from repository_context.context import Context
import subprocess
import os

IMAGES_DIR = "/var/lib/jenkins/images"
REGISTRY_URI = os.getenv("REGISTRY_URI")


def build_standalone_image(
    ctx: Context, base_image_name: str, project_name: str
) -> str:
    print(f"Building standalone image for {project_name}...")
    image_path = os.path.join(IMAGES_DIR, ctx.language.value, "Dockerfile.standalone")
    print(f"Dockerfile path: {image_path}")
    image_name = f"{base_image_name}-{project_name}"
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
    return image_name


def build_base_image(ctx: Context, base_image_name: str) -> str:
    print(f"Building base image for {ctx.language.name}...")
    return "z"


def tag_image(image_name: str, tag: str) -> None:
    print(f"Tagging image {image_name} with {tag}...")
    command = [
        "docker",
        "tag",
        image_name,
        tag,
    ]
    subprocess.run(command)
    return None


def push_image(tag: str) -> None:
    print(f"Pushing image {tag}...")
    command = [
        "docker",
        "push",
        tag,
    ]
    subprocess.run(command)
    return None


def docker_image_build(ctx: Context, base_image_name: str, project_name: str) -> None:
    final_image_name = ""
    if ctx.standalone:
        final_image_name = build_standalone_image(ctx, base_image_name, project_name)
    else:
        final_image_name = build_base_image(ctx, base_image_name)
    tag = f"{REGISTRY_URI}/{final_image_name}"

    tag_image(final_image_name, tag)
    push_image(tag)
    return None
