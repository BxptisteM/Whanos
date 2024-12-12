import subprocess

def gcloud_auth() -> None:
    print("Authenticating with GCP...")
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
    
    