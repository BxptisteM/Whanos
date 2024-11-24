from termcolor import colored
import subprocess
import os


def ks_setup() -> None:
    print(colored("Setting up Kubespray...", "yellow"))
    image_dir = os.getcwd() + "/cli/cluster/kubespray"
    subprocess.run(
        ["docker", "build", "-t", "whanos-kubespray", "."],
        cwd=image_dir,
    )
    print(colored("Kubespray image setup complete!", "green"))
