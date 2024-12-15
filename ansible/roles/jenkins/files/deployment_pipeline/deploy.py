import repository_context
import docker_manager
import k8s_manager


def deploy(project_name: str) -> None:
    print(f"Deploying {project_name}...")
    ctx = repository_context.get(project_name)
    print(f"Detected language: {ctx.language.value}")
    print(f"Standalone: {ctx.standalone}")
    image_name = docker_manager.run(ctx)
    if ctx.deployable:
        k8s_manager.run(ctx, image_name)
