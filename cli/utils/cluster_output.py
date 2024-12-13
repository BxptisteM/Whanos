from pathlib import Path
import subprocess

TERRAFORM_DIR = Path("terraform/cluster")


def get_cluster_region():
    return subprocess.check_output(
        ["terraform", "output", "-raw", "region"],
        text=True,
        cwd=TERRAFORM_DIR,
    ).strip()


def get_cluster_name():
    return subprocess.check_output(
        ["terraform", "output", "-raw", "kubernetes_cluster_name"],
        text=True,
        cwd=TERRAFORM_DIR,
    ).strip()
