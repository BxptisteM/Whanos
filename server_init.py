import os
from pathlib import Path
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
import subprocess
from termcolor import colored
import time

load_dotenv()

HARD_CODED_VALUES = {
    "region": "europe-west1",
    "zone": "europe-west1-d",
    "vm_name": "whanos-vm",
    "machine_type": "e2-small",
    "image": "projects/debian-cloud/global/images/debian-12-bookworm-v20241112",
    "disk_type": "pd-balanced",
    "disk_size": 10
}


def authenticate_gcloud():
    print(colored("Authenticating with Google Cloud...", "yellow"))
    process = subprocess.Popen(
        ["gcloud", "auth", "login", "--no-launch-browser"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    for line in process.stdout:
        if "https://" in line:
            print(colored("Follow this link to authenticate:", "cyan"))
            print(colored(line.strip(), "blue"))
            print(colored("Then enter the given code:", "cyan"))

    process.wait()

    if process.returncode != 0:
        raise Exception(colored("Failed to authenticate with gcloud. Please check your setup.", "red"))


def configure_gcloud_project(project_id):
    print(colored(f"Configuring GCP project: {project_id}...", "yellow"))
    process = subprocess.run(
        ["gcloud", "config", "set", "project", project_id],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if process.returncode != 0:
        raise Exception(colored(f"Failed to set GCP project to {project_id}.", "red"))

    print(colored(f"Project configured successfully: {project_id}", "green"))


def get_user_variables():
    ssh_key_path = os.getenv("SSH_PUBLIC_KEY_PATH")
    ssh_username = os.getenv("SSH_USERNAME")
    private_key_path = os.getenv("SSH_PRIVATE_KEY_PATH")

    if not ssh_key_path or not ssh_username or not private_key_path:
        raise ValueError(colored("SSH_PUBLIC_KEY_PATH, SSH_USERNAME, and SSH_PRIVATE_KEY_PATH must be defined in the .env file", "red"))

    ssh_key_path = Path(ssh_key_path).expanduser()
    private_key_path = Path(private_key_path).expanduser()

    if not ssh_key_path.exists():
        raise FileNotFoundError(colored(f"SSH key not found: {ssh_key_path}", "red"))
    if not private_key_path.exists():
        raise FileNotFoundError(colored(f"Private SSH key not found: {private_key_path}", "red"))

    with ssh_key_path.open("r") as f:
        ssh_public_key = f.read().strip()

    return {
        "ssh_keys": f"{ssh_username}:{ssh_public_key}",
        "ssh_username": ssh_username,
        "private_key_path": private_key_path
    }


def generate_terraform_tfvars(project_id, user_vars):
    env = Environment(loader=FileSystemLoader("terraform/template"))
    template = env.get_template("terraform.tfvars.j2")

    output_content = template.render(
        project_id=project_id,
        **HARD_CODED_VALUES,
        **user_vars
    )

    tfvars_path = Path("terraform/terraform.tfvars")
    with tfvars_path.open("w") as f:
        f.write(output_content)

    print(colored(f"Terraform configuration file generated: {tfvars_path}", "green"))


def run_terraform():
    terraform_dir = Path("terraform")

    print(colored("Initializing Terraform...", "yellow"))
    subprocess.run(["terraform", "init"], cwd=terraform_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    print(colored("Applying Terraform configuration...", "yellow"))
    process = subprocess.run(["terraform", "apply", "-auto-approve"], cwd=terraform_dir, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=True)

    if process.returncode != 0:
        raise Exception(colored(f"Terraform apply failed:\n{process.stderr}", "red"))

    print(colored("Terraform apply complete!", "green"))

    output_process = subprocess.run(
        ["terraform", "output", "vm_external_ip"],
        cwd=terraform_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

    if output_process.returncode != 0 or not output_process.stdout.strip():
        raise Exception(colored("Failed to retrieve VM external IP. Ensure Terraform outputs are correctly defined.", "red"))

    vm_ip = output_process.stdout.strip().replace('"', '')
    return vm_ip


def update_ansible_inventory(vm_ip, ssh_username, private_key_path):
    ansible_dir = Path("ansible")
    inventory_path = ansible_dir / "inventory"

    ansible_dir.mkdir(exist_ok=True)

    inventory_entry = f"""[jenkins]
{vm_ip} ansible_user={ssh_username} ansible_ssh_private_key_file={private_key_path}"""

    if inventory_path.exists():
        with inventory_path.open("r") as f:
            current_content = f.read()

        if inventory_entry.strip() != current_content.strip():
            with inventory_path.open("w") as f:
                f.write(inventory_entry)
            print(colored("Inventory file updated.", "green"))
        else:
            print(colored("Inventory file is already up-to-date.", "yellow"))
    else:
        with inventory_path.open("w") as f:
            f.write(inventory_entry)
        print(colored("Inventory file created.", "green"))


def remove_old_ssh_key(vm_ip):
    known_hosts_path = Path.home() / ".ssh" / "known_hosts"
    subprocess.run(["ssh-keygen", "-f", str(known_hosts_path), "-R", vm_ip], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(colored(f"Old SSH key for {vm_ip} removed from {known_hosts_path}.", "green"))


if __name__ == "__main__":
    try:
        print(colored("Welcome to the GCP VM Terraform setup script!", "cyan"))
        authenticate_gcloud()
        project_id = input(colored("Enter your GCP project ID: ", "cyan")).strip()
        configure_gcloud_project(project_id)
        user_vars = get_user_variables()
        generate_terraform_tfvars(project_id, user_vars)
        vm_ip = run_terraform()

        ssh_username = user_vars["ssh_username"]
        private_key_path = user_vars["private_key_path"]

        update_ansible_inventory(vm_ip, ssh_username, private_key_path)
        remove_old_ssh_key(vm_ip)

        print(colored("\nYou successfully created your VM on GCP!", "green"))
        subprocess.run("export $(grep -v '^#' .env | xargs)", shell=True, check=True)
        print(colored("Installing Jenkins on your VM...", "yellow"))
        time.sleep(10)
        subprocess.run("ansible-playbook -i ansible/inventory ansible/jenkins.yml", shell=True, check=True)
        print(colored("Jenkins is now installed on your VM!", "green"))
        print(colored("You can access it via SSH using the following command:", "cyan"))
        print(colored(f"ssh {ssh_username}@{vm_ip}", "blue"))
    except Exception as e:
        print(colored(f"Error: {e}", "red"))
