from pathlib import Path
import subprocess


def get_vm_ip() -> str:
    terraform_dir = Path("terraform/master")
    output = subprocess.run(
        ["terraform", "output", "vm_external_ip"],
        cwd=terraform_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=True,
    )
    return output.stdout.decode().strip().replace('"', "")
