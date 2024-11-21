import subprocess
import os
from jinja2 import Environment, FileSystemLoader
from termcolor import colored
from pathlib import Path

HARD_CODED_VALUES = {
    "region": "europe-west1",
    "zone": "europe-west1-d",
    "vm_name": "whanos-vm",
    "machine_type": "e2-small",
    "image": "projects/debian-cloud/global/images/debian-12-bookworm-v20241112",
    "disk_type": "pd-balanced",
    "disk_size": 10
}

def get_user_variables():
    ssh_key_path = os.getenv("SSH_PUBLIC_KEY_PATH")
    ssh_username = os.getenv("SSH_USERNAME")

    if not ssh_key_path or not ssh_username:
        raise ValueError(colored("SSH_PUBLIC_KEY_PATH and SSH_USERNAME must be defined in the .env file", "red"))

    ssh_key_path = Path(ssh_key_path).expanduser()
    if not ssh_key_path.exists():
        raise FileNotFoundError(colored(f"SSH key not found: {ssh_key_path}", "red"))

    with ssh_key_path.open("r") as f:
        ssh_public_key = f.read().strip()

    return {
        "ssh_keys": f"{ssh_username}:{ssh_public_key}"
    }


def terraform_generate_tfvars(project_id, user_vars):
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


def terraform_run():
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
