from language.detect import detect


def deploy(project_name: str) -> None:
    print(f"Deploying {project_name}...")
    language = detect()
    print(f"Detected language: {language.name}")
