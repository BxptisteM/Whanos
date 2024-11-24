import subprocess
import os
from typing import List
from termcolor import colored
from cli.cluster.kubespray.path import KUBESPRAY_DIR


def build_ip_list(vm_ips: List[str]) -> str:
    """Builds a space-separated string of IP addresses."""
    return " ".join(vm_ips)


def run(vm_ips: List[str]) -> None:
    """Automates the Kubespray setup process."""
    ssh_key_path = os.getenv("SSH_PRIVATE_KEY_PATH")
    if not os.path.exists(ssh_key_path):
        print(colored("Error: SSH key not found at ~/.ssh/id_rsa", "red"))
        return

    docker_run_cmd = [
        "docker",
        "run",
        "--rm",
        "-it",
        "--mount",
        f"type=bind,source={ssh_key_path},target=/root/.ssh/id_rsa",
        "whanos-kubespray:latest",
        "bash",
        "-c",
        f"""
        cp -rfp inventory/sample inventory/mycluster && \
        CONFIG_FILE=inventory/mycluster/hosts.yaml python3 contrib/inventory_builder/inventory.py {build_ip_list(vm_ips)} && \
        cat inventory/mycluster/hosts.yaml && \
        ansible-playbook -i inventory/mycluster/hosts.yaml --private-key /root/.ssh/id_rsa cluster.yml -u {os.getenv("SSH_USERNAME")}
        """,
    ]

    # Execute the command
    print(colored("Launching Docker container and running Kubespray setup...", "green"))
    try:
        subprocess.run(docker_run_cmd, check=True)
        print(colored("Kubespray setup completed successfully.", "green"))
    except subprocess.CalledProcessError as e:
        print(colored(f"Error during Kubespray setup: {e}", "red"))
