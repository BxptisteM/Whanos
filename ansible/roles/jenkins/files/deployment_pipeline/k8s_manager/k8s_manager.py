from repository_context.context import Context


def run(ctx: Context) -> None:
    print("K8S MANAGER", "=" * 60)
    print(f"Deploying {ctx.project_name} to cluster...")
    print("Deployment properties:")
