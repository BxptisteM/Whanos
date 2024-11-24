import os
from termcolor import colored


def install() -> None:
    print(colored("Welcome to the Whanos Project installation script!", "cyan"))
    install_ansible()


def install_ansible() -> None:
    print(colored("Installing Ansible...", "yellow"))
    os.system("sudo apt update")
    os.system("sudo apt install -y ansible")
    print(colored("Ansible installed successfully!", "green"))
