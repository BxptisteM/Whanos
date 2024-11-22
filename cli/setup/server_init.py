import os
from dotenv import load_dotenv
from termcolor import colored
import cli.setup.gcloud_setup as gcloud_setup
import cli.setup.master_vm as master_vm

load_dotenv()


def server_init():
    try:
        print(colored("Welcome to the GCP VM Terraform setup script!", "cyan"))
        gcloud_setup.gcloud_auth()
        project_id = input(colored("Enter your GCP project ID: ", "cyan")).strip()
        gcloud_setup.gcloud_project_configuration(project_id)
        user_vars = master_vm.get_user_variables()
        master_vm.terraform_generate_tfvars(project_id, user_vars)
        vm_ip = master_vm.terraform_run()
        ssh_username = os.getenv("SSH_USERNAME")
        print(colored("\nYou successfully created your VM on GCP!", "green"))
        print(colored("You can access it via SSH using the following command:", "cyan"))
        print(colored(f"ssh {ssh_username}@{vm_ip}", "blue"))
    except Exception as e:
        print(colored(f"Error: {e}", "red"))
