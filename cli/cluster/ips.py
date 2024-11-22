from typing import List
import os
import subprocess


def get_vm_ips() -> List[str]:
    """Get the list of terraform outputs for the cluster"""
    terraform_dir = os.getcwd() + "/terraform"
    try:
        result = subprocess.run(
            ["terraform", "output", "k8s_node_ips"],
            cwd=terraform_dir,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
        output = result.stdout
        return [
            ip.strip()
            for ip in output.strip()[1:-1].replace('"', "").split(",")
            if ip.strip()
        ]
    except subprocess.CalledProcessError as e:
        print("Error running terraform.")
        return []
