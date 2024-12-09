from repository_context.context import Context
from docker_manager.image_builder import docker_image_build


def get_base_image_name(ctx: Context) -> str:
    return f"whanos-{ctx.language.value}"


def run(ctx: Context, project_name: str) -> None:
    base_image_name = get_base_image_name(ctx)
    docker_image_build(ctx, base_image_name, project_name)
