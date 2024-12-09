from repository_context.context import Context
import subprocess
import os

IMAGES_DIR = "/var/lib/jenkins/images"


def build_standalone_image(
    ctx: Context, base_image_name: str, project_name: str
) -> None:
    print(f"Building standalone image for {project_name}...")
    image_path = os.path.join(IMAGES_DIR, ctx.language.value, "Dockerfile.standalone")
    print(f"Dockerfile path: {image_path}")
    image_name = f"{base_image_name}-{project_name}:latest"
    print(f"Image name: {image_name}")
    subprocess.run(
        [
            "docker",
            "build",
            "-t",
            image_name,
            "-f",
            image_path,
            ".",
        ]
    )
    return None


def build_base_image(ctx: Context, base_image_name: str) -> None:
    print(f"Building base image for {ctx.language.name}...")
    return None


def docker_image_build(ctx: Context, base_image_name: str, project_name: str) -> None:
    if ctx.standalone:
        build_standalone_image(ctx, base_image_name, project_name)
    else:
        build_base_image(ctx, base_image_name)
    return None
