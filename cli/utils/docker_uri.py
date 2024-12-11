from cli.utils.project_id import get_project_id

def get_docker_uri() -> str:
    zone = "europe-west1-docker.pkg.dev"
    proj_id = get_project_id()
    repo_name = f"{proj_id}-docker-repository"
    return f"{zone}/{proj_id}/{repo_name}"
