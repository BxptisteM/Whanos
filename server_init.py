import os
from dotenv import load_dotenv
from termcolor import colored
from cli.gcloud_setup import *
from cli.master_vm import *

load_dotenv()

if __name__ == "__main__":
    try:
        print(colored("Welcome to the GCP VM Terraform setup script!", "cyan"))
        gcloud_auth()
        project_id = input(colored("Enter your GCP project ID: ", "cyan")).strip()
        gcloud_project_configuration(project_id)
        user_vars = get_user_variables()
        terraform_generate_tfvars(project_id, user_vars)
        vm_ip = terraform_run()
        ssh_username = os.getenv("SSH_USERNAME")
        print(colored("\nYou successfully created your VM on GCP!", "green"))
        print(colored("You can access it via SSH using the following command:", "cyan"))
        print(colored(f"ssh {ssh_username}@{vm_ip}", "blue"))
    except Exception as e:
        print(colored(f"Error: {e}", "red"))
