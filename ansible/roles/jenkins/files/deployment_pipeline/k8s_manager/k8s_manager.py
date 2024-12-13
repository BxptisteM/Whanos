from repository_context.context import Context
import subprocess


def run(ctx: Context) -> None:
    print("K8S MANAGER", "=" * 60)
    print(f"Deploying {ctx.project_name} to cluster...")
    res = subprocess.run(
        ["kubectl", "get", "pods", "--all-namespaces"], capture_output=True, text=True
    )
    print(res.stdout)
