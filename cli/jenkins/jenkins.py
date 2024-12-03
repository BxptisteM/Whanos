from termcolor import colored
from cli.jenkins.inventory import jenkins_generate_inventory
from cli.utils.vm_ip import get_vm_ip
from cli.utils.user_vars import get_user_variables
import subprocess


def jenkins():
    print(colored("Setting up Jenkins...", "yellow"))
    vm_ip = get_vm_ip()
    user_vars = get_user_variables()
    jenkins_generate_inventory(
        vm_ip, user_vars["ssh_username"], user_vars["private_key_path"]
    )
    run_playbook()


def run_playbook():
    print(colored("Running the jenkins playbook...", "yellow"))
    subprocess.run("export $(grep -v '^#' .env | xargs)", shell=True, check=True)
    subprocess.run(
        "ansible-playbook -i ansible/inventory ansible/jenkins.yml",
        shell=True,
        check=True,
    )
    print(colored("Jenkins is now installed on your VM!", "green"))
