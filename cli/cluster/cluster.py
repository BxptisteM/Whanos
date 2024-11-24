import cli.cluster.ips as ips
import cli.cluster.kubespray.ks as ks
from pathlib import Path
from cli.cluster.kubespray.setup import ks_setup


def cluster() -> None:
    ks_setup()
    vm_ips = ips.get_vm_ips()
    ks.run(vm_ips)
