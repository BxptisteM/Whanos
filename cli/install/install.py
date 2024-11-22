import os
from termcolor import colored
import subprocess
from pathlib import Path


def install() -> None:
    print(colored("Welcome to the Whanos Project installation script!", "cyan"))
    install_ansible()
    install_kubespray()


def install_ansible() -> None:
    print(colored("Installing Ansible...", "yellow"))
    os.system("sudo apt update")
    os.system("sudo apt install -y ansible")
    print(colored("Ansible installed successfully!", "green"))


def install_kubespray() -> None:
    print(colored("Installing Kubespray...", "yellow"))
    home_dir = Path.home()

    repo_url = "https://github.com/kubernetes-incubator/kubespray.git"
    clone_dir = home_dir / "kubespray"

    if not clone_dir.exists():
        print(colored(f"Cloning repository into {clone_dir}...", "yellow"))
        try:
            subprocess.run(["git", "clone", repo_url, str(clone_dir)], check=True)
        except subprocess.CalledProcessError as e:
            print(colored(f"Error cloning the repository: {e}", "red"))
            return
    else:
        print(
            colored(
                f"Repository already exists at {clone_dir}. Skipping clone.", "yellow"
            )
        )

    requirements_file = clone_dir / "requirements.txt"
    if requirements_file.exists():
        print(colored("Installing dependencies from requirements.txt...", "yellow"))
        try:
            subprocess.run(["pip", "install", "-r", str(requirements_file)], check=True)
        except subprocess.CalledProcessError as e:
            print(colored(f"Error installing dependencies: {e}", "red"))
            return
    else:
        print(colored(f"requirements.txt not found at {requirements_file}.", "red"))
        return
    print(colored("Kubespray installed successfully!", "green"))
