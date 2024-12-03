from termcolor import colored
from pathlib import Path


def jenkins_generate_inventory(
    vm_ip: str, ssh_username: str, private_key_path: str
) -> None:
    ansible_dir = Path("ansible")
    inventory_path = ansible_dir / "inventory"

    ansible_dir.mkdir(exist_ok=True)

    inventory_entry = f"""[jenkins]
{vm_ip} ansible_user={ssh_username} ansible_ssh_private_key_file={private_key_path}"""

    if inventory_path.exists():
        with inventory_path.open("r") as f:
            current_content = f.read()

        if inventory_entry.strip() != current_content.strip():
            with inventory_path.open("w") as f:
                f.write(inventory_entry)
            print(colored("Inventory file updated.", "green"))
        else:
            print(colored("Inventory file is already up-to-date.", "yellow"))
    else:
        with inventory_path.open("w") as f:
            f.write(inventory_entry)
        print(colored("Inventory file created.", "green"))
