import subprocess
import os


CLUSTER_NAME = os.getenv("CLUSTER_NAME")
CLUSTER_REGION = os.getenv("CLUSTER_REGION")


def gcloud_auth() -> None:
    print("GCLOUD AUTH", "=" * 60)
    res = subprocess.run(
        [
            "gcloud",
            "auth",
            "activate-service-account",
            "--key-file",
            "/var/lib/jenkins/jenkins-sa-key.json",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    print(res.stdout)
    res = subprocess.run(
        [
            "gcloud",
            "auth",
            "configure-docker",
            "europe-west1-docker.pkg.dev",
            "--quiet",
        ],
        capture_output=True,
        text=True,
    )
    print(res.stdout)
    res = subprocess.run(
        [
            "gcloud",
            "container",
            "clusters",
            "get-credentials",
            CLUSTER_NAME,
            "--region",
            CLUSTER_REGION,
        ],
        capture_output=True,
        text=True,
    )
    print(res.stdout)
