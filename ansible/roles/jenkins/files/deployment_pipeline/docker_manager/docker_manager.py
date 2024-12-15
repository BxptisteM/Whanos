from repository_context.context import Context
from docker_manager.image_builder import docker_image_build


def get_base_image_name(ctx: Context) -> str:
    return f"whanos-{ctx.language.value}"


def run(ctx: Context) -> str:
    print("DOCKER MANAGER", "=" * 60)
    base_image_name = get_base_image_name(ctx)
    return docker_image_build(ctx, base_image_name)
