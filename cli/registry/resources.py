from termcolor import colored
from pathlib import Path
import subprocess


def generate_registry_resource():
    print(colored("Applying Docker registry...", "yellow"))
    terraform_dir = Path("terraform/registry")
    print(colored("Initializing Terraform...", "yellow"))
    subprocess.run(
        ["terraform", "init"],
        cwd=terraform_dir,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )

    print(colored("Applying Terraform configuration...", "yellow"))
    process = subprocess.run(
        ["terraform", "apply", "-auto-approve"],
        cwd=terraform_dir,
        stderr=subprocess.PIPE,
        text=True,
    )

    if process.returncode != 0:
        raise Exception(colored(f"Terraform apply failed:\n{process.stderr}", "red"))

    print(colored("Terraform apply complete!", "green"))
