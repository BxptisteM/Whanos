import repository_context
import docker_manager


def deploy(project_name: str) -> None:
    print(f"Deploying {project_name}...")
    ctx = repository_context.get()
    print(f"Detected language: {ctx.language.value}")
    print(f"Standalone: {ctx.standalone}")
    docker_manager.run(ctx, project_name)
