import subprocess
from cli.utils.project_id import get_project_id
import os

SERVICE_ACCOUNT_NAME = "jenkins-sa"
PROJECT_ID = get_project_id()
OUTPUT_DIR = "ansible/roles/jenkins/files"


def service_account():
    if os.path.exists(os.path.join(OUTPUT_DIR, f"{SERVICE_ACCOUNT_NAME}-key.json")):
        print("Service account already exists, skipping creation...")
        return
    create_service_account()
    assign_gke_role()
    assign_container_registry_role()
    create_service_account_key()


def create_service_account():
    command = [
        "gcloud",
        "iam",
        "service-accounts",
        "create",
        SERVICE_ACCOUNT_NAME,
        "--description",
        "Service account for GKE and Container Registry access",
    ]
    print("Creating service account...")
    subprocess.run(command, check=True)


def assign_gke_role():
    command = [
        "gcloud",
        "projects",
        "add-iam-policy-binding",
        PROJECT_ID,
        "--member",
        f"serviceAccount:{SERVICE_ACCOUNT_NAME}@{PROJECT_ID}.iam.gserviceaccount.com",
        "--role",
        "roles/container.developer",
    ]
    print("Assigning GKE role...")
    subprocess.run(command, check=True)


def assign_container_registry_role():
    command = [
        "gcloud",
        "projects",
        "add-iam-policy-binding",
        PROJECT_ID,
        "--member",
        f"serviceAccount:{SERVICE_ACCOUNT_NAME}@{PROJECT_ID}.iam.gserviceaccount.com",
        "--role",
        "roles/artifactregistry.writer",
    ]
    command2 = [
        "gcloud",
        "projects",
        "add-iam-policy-binding",
        PROJECT_ID,
        "--member",
        f"serviceAccount:{SERVICE_ACCOUNT_NAME}@{PROJECT_ID}.iam.gserviceaccount.com",
        "--role",
        "roles/artifactregistry.reader",
    ]
    print("Assigning Container Registry role...")
    subprocess.run(command, check=True)
    subprocess.run(command2, check=True)

def create_service_account_key():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    key_file_path = os.path.join(OUTPUT_DIR, f"{SERVICE_ACCOUNT_NAME}-key.json")
    command = [
        "gcloud",
        "iam",
        "service-accounts",
        "keys",
        "create",
        key_file_path,
        "--iam-account",
        f"{SERVICE_ACCOUNT_NAME}@{PROJECT_ID}.iam.gserviceaccount.com",
    ]
    print(f"Creating service account key in {key_file_path}...")
    subprocess.run(command, check=True)
