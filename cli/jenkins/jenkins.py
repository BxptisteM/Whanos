from termcolor import colored
from cli.jenkins.inventory import jenkins_generate_inventory
from cli.utils.vm_ip import get_vm_ip
from cli.utils.docker_uri import get_docker_uri
from cli.utils.project_id import get_project_id
from cli.utils.user_vars import get_user_variables
from cli.jenkins.vars import jenkins_var
from cli.jenkins.service_account import service_account
# from cli.utils.cluster_output import get_cluster_name, get_cluster_region
import subprocess


def jenkins():
    print(colored("Setting up Jenkins...", "yellow"))
    vm_ip = get_vm_ip()
    user_vars = get_user_variables()
    project_id = get_project_id()
    registry_uri = get_docker_uri()
    # cluster_name = get_cluster_name()
    # cluster_region = get_cluster_region()
    jenkins_generate_inventory(
        vm_ip, user_vars["ssh_username"], user_vars["private_key_path"]
    )
    service_account()
    jenkins_var("jenkins_vm_ip", vm_ip)
    jenkins_var("project_id", project_id)
    jenkins_var("registry_uri", registry_uri)
    jenkins_var("cluster_name", "clean-evening-442413-k4-gke")
    jenkins_var("cluster_region", "europe-west1")
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
