import os
from termcolor import colored
from pathlib import Path


def get_user_variables() -> dict:
    ssh_key_path = os.getenv("SSH_PUBLIC_KEY_PATH")
    ssh_username = os.getenv("SSH_USERNAME")
    private_key_path = os.getenv("SSH_PRIVATE_KEY_PATH")

    if not ssh_key_path or not ssh_username or not private_key_path:
        raise ValueError(
            colored(
                "SSH_PUBLIC_KEY_PATH, SSH_USERNAME, and SSH_PRIVATE_KEY_PATH must be defined in the .env file",
                "red",
            )
        )

    ssh_key_path = Path(ssh_key_path).expanduser()
    private_key_path = Path(private_key_path).expanduser()

    if not ssh_key_path.exists():
        raise FileNotFoundError(colored(f"SSH key not found: {ssh_key_path}", "red"))
    if not private_key_path.exists():
        raise FileNotFoundError(
            colored(f"Private SSH key not found: {private_key_path}", "red")
        )

    with ssh_key_path.open("r") as f:
        ssh_public_key = f.read().strip()

    return {
        "ssh_keys": f"{ssh_username}:{ssh_public_key}",
        "ssh_username": ssh_username,
        "private_key_path": private_key_path,
    }
