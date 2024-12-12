from termcolor import colored
import subprocess
from cli.utils.cluster_output import get_cluster_name, get_cluster_region


def configure_kubectl():
    print(colored("Configuring kubectl to connect to the cluster...", "cyan"))
    try:
        kubernetes_cluster_name = get_cluster_name()

        region = get_cluster_region()

        gcloud_command = [
            "gcloud",
            "container",
            "clusters",
            "get-credentials",
            kubernetes_cluster_name,
            "--region",
            region,
        ]

        subprocess.run(gcloud_command, check=True)
        print(
            colored(
                "Successfully configured kubectl!",
            )
        )

    except subprocess.CalledProcessError as e:
        print(colored(f"Command failed with error: {e}", "red"))
    except FileNotFoundError:
        print(
            colored(
                "Make sure gcloud and terraform are installed and available in PATH.",
                "red",
            )
        )
