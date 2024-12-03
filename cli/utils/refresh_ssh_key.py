from pathlib import Path
import subprocess
from termcolor import colored


def remove_old_ssh_key(vm_ip):
    known_hosts_path = Path.home() / ".ssh" / "known_hosts"
    subprocess.run(
        ["ssh-keygen", "-f", str(known_hosts_path), "-R", vm_ip],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print(colored(f"Old SSH key for {vm_ip} removed from {known_hosts_path}.", "green"))
