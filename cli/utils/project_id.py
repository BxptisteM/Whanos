import subprocess


def get_project_id():
    result = subprocess.run(
        ["gcloud", "config", "get-value", "project"],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()
