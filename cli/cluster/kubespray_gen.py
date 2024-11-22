from typing import List, Dict
import os
from termcolor import colored
import yaml


INVENTORY_PATH="/ansible/inventory/cluster/"
HOSTS_FILENAME="hosts.yaml"

def handle_inventory_path(inventory_path: str) -> None:
    """Check if the inventory file exists"""
    if os.path.exists(inventory_path):
        return
    else:
        print(colored(f"Generating inventory file at {inventory_path}...", "yellow"))
        os.makedirs(os.path.dirname(inventory_path), exist_ok=True)


def handle_hosts_file(hosts_file_path: str) -> None:
    """Check if the hosts file exists"""
    if os.path.exists(hosts_file_path):
        with open(hosts_file_path, "w") as file:
            file.truncate(0)
    else:
        print(colored(f"Generating hosts file at {hosts_file_path}...", "yellow"))
        with open(hosts_file_path, "w") as file:
            pass


def generate_config_dict(vm_ips: List[str]) -> Dict:
    """
    Generate the Kubespray hosts.yaml structure.
    """
    control_plane_ip = vm_ips[0]
    worker_ips = vm_ips[1:]

    hosts_structure = {
        "all": {
            "hosts": {
                control_plane_ip: {
                    "ansible_host": control_plane_ip,
                    "ip": control_plane_ip,
                    "access_ip": control_plane_ip,
                },
                **{
                    worker_ip: {
                        "ansible_host": worker_ip,
                        "ip": worker_ip,
                        "access_ip": worker_ip,
                    }
                    for worker_ip in worker_ips
                },
            },
            "children": {
                "k8s_cluster": {
                    "children": {
                        "kube_control_plane": {"hosts": {control_plane_ip: None}},
                        "kube_node": {"hosts": {ip: None for ip in vm_ips}},
                        "etcd": {"hosts": {control_plane_ip: None}},
                    },
                },
                "calico_rr": {"hosts": {}},
            },
        }
    }
    return hosts_structure


def write_config_to_file(config_dict: Dict, hosts_file_path: str) -> None:
    with open(hosts_file_path, "w") as file:
        yaml.dump(config_dict, file, default_flow_style=False)
    print(
        colored(
            f"Kubespray hosts.yaml file generated successfully at {hosts_file_path}!",
            "green",
        )
    )


def generate_kubespray_file(vm_ips: List[str]) -> None:
    if not vm_ips:
        raise ValueError("No IPs found in the Terraform output")
    inventory_path = os.getcwd() + INVENTORY_PATH
    hosts_file_path = inventory_path + HOSTS_FILENAME
    handle_inventory_path(inventory_path)
    handle_hosts_file(hosts_file_path)
    config_dict = generate_config_dict(vm_ips)
    write_config_to_file(config_dict, hosts_file_path)
