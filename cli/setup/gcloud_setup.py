from termcolor import colored
import subprocess

def gcloud_auth():
    print(colored("Authenticating with Google Cloud...", "yellow"))
    process = subprocess.Popen(
        ["gcloud", "auth", "login", "--no-launch-browser"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    for line in process.stdout:
        if "https://" in line:
            print(colored("Follow this link to authenticate:", "cyan"))
            print(colored(line.strip(), "blue"))
            print(colored("Then enter the given code:", "cyan"))

    process.wait()

    if process.returncode != 0:
        raise Exception(colored("Failed to authenticate with gcloud. Please check your setup.", "red"))
    
def gcloud_project_configuration(project_id):
    print(colored(f"Configuring GCP project: {project_id}...", "yellow"))
    process = subprocess.run(
        ["gcloud", "config", "set", "project", project_id],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if process.returncode != 0:
        raise Exception(colored(f"Failed to set GCP project to {project_id}.", "red"))

    print(colored(f"Project configured successfully: {project_id}", "green"))
