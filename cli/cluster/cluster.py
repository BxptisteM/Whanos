import cli.cluster.ips as ips
import cli.cluster.kubespray_gen as kubespray_gen


def cluster() -> None:
    vm_ips = ips.get_vm_ips()
    kubespray_gen.generate_kubespray_file(vm_ips)
