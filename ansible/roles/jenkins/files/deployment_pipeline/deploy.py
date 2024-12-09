import repository_context

def deploy(project_name: str) -> None:
    print(f"Deploying {project_name}...")
    ctx = repository_context.get()
    print(f"Detected language: {ctx.language.name}")
    print(f"Standalone: {ctx.standalone}")
