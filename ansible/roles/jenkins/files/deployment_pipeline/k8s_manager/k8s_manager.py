from repository_context.context import Context
import subprocess


def run(ctx: Context) -> None:
    print(f"Deploying {ctx.project_name} to cluster...")
    subprocess.run(["kubectl", "get", "pods", "--all-namespaces"])
