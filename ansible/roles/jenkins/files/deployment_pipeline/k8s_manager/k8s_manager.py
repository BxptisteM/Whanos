from repository_context.context import Context
import subprocess


def run(ctx: Context) -> None:
    print("K8S MANAGER", "=" * 60)
    print(f"Deploying {ctx.project_name} to cluster...")
    print("Deployment properties:")
    print("Ports: ", ctx.deployment_props.ports)
    print("Resources: ", ctx.deployment_props.resources)
    print("Replicas: ", ctx.deployment_props.replicas)
