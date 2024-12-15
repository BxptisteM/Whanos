from repository_context.context import Context
import os
import subprocess

REGISTRY_URI = os.getenv("REGISTRY_URI")
CHART_FILEPATH = "/var/lib/jenkins/kubernetes/helm/whanos-app"


def add_image_values(ctx: Context, image_name: str) -> None:
    yaml_content = f"""
image:
  name: {ctx.project_name.replace("_", "-")}
  uri: {REGISTRY_URI}/{image_name}:latest
    """
    with open("whanos.yml", "a") as file:
        file.write(yaml_content)


def check_if_deployment_exists(ctx: Context) -> bool:
    cmd = [
        "kubectl",
        "get",
        "deployment",
        "--namespace",
        ctx.project_name.replace("_", "-"),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.split("\n").__len__() > 1
    except subprocess.CalledProcessError as e:
        print(f"Error checking for existing release: {e}", flush=True)
        raise


def run_deployment(ctx: Context) -> None:
    namespace = ctx.project_name.replace("_", "-")
    default_val_file = CHART_FILEPATH + "/values.yaml"
    release_name = f"{namespace}-release"
    with open(default_val_file, "r") as file:
        print(f"Default values file contents: {file.read()}", flush=True)
    with open("whanos.yml", "r") as file:
        print(f"Whanos values file contents: {file.read()}", flush=True)

    if not check_if_deployment_exists(ctx):
        print("No existing release found. Performing first-time install...", flush=True)
        command = [
            "helm",
            "install",
            release_name,
            CHART_FILEPATH,
            "-f",
            default_val_file,
            "-f",
            "whanos.yml",
            "--namespace",
            namespace,
            "--create-namespace",
        ]
    else:
        print("Existing release found. Updating deployment...", flush=True)
        
        command_helm = [
            "helm",
            "upgrade",
            release_name,
            CHART_FILEPATH,
            "-f",
            default_val_file,
            "-f",
            "whanos.yml",
            "--namespace",
            namespace,
        ]

        command = [
            "kubectl",
            "rollout",
            "restart",
            f"deployment/{release_name}-deployment",
            "-n",
            namespace,
        ]

        try:
            subprocess.run(command_helm, check=True, capture_output=True, text=True)
            subprocess.run(command, check=True, capture_output=True, text=True)
            print("Deployment updated successfully", flush=True)
            return
        except subprocess.CalledProcessError as e:
            print(f"Deployment update failed: {e}", flush=True)
            raise

    print(f"Running command: {' '.join(command)}", flush=True)
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Command output: {result.stdout}", flush=True)
    except subprocess.CalledProcessError as e:
        print(f"Helm command failed with return code {e.returncode}", flush=True)
        print(f"Error output: {e.stderr}", flush=True)
        raise


def run(ctx: Context, image_name: str) -> None:
    print("K8S MANAGER", "=" * 60)
    print(f"Deploying {ctx.project_name} to cluster...")
    add_image_values(ctx, image_name)
    run_deployment(ctx)
