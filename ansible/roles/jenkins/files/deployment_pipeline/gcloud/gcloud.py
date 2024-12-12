import subprocess
import os


CLUSTER_NAME = os.getenv("CLUSTER_NAME")
CLUSTER_REGION = os.getenv("CLUSTER_REGION")


def gcloud_auth() -> None:
    print("Authenticating with GCP and configuring...")
    subprocess.run(
        [
            "gcloud",
            "auth",
            "activate-service-account",
            "--key-file",
            "/var/lib/jenkins/jenkins-sa-key.json",
        ],
        check=True,
    )
    subprocess.run(
        [
            "gcloud",
            "auth",
            "configure-docker",
            "europe-west1-docker.pkg.dev",
            "--quiet",
        ]
    )
    subprocess.run(
        [
            "gcloud",
            "container",
            "clusters",
            "get-credentials",
            CLUSTER_NAME,
            "--region",
            CLUSTER_REGION,
        ]
    )
