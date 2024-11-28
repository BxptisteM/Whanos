from pathlib import Path
import subprocess
from termcolor import colored


def cluster() -> None:
    print(colored("Configuring kubectl to connect to the cluster...", "cyan"))
    terraform_dir = Path("terraform")
    try:
        kubernetes_cluster_name = subprocess.check_output(
            ["terraform", "output", "-raw", "kubernetes_cluster_name"],
            text=True,
            cwd=terraform_dir,
        ).strip()

        region = subprocess.check_output(
            ["terraform", "output", "-raw", "region"], text=True, cwd=terraform_dir
        ).strip()

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
