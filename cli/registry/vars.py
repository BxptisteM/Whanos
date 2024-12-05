from termcolor import colored
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from cli.utils.project_id import get_project_id

HARD_CODED_VALUES = {
    "region": "europe-west1",
}


def terraform_generate_registry_tfvars():
    env = Environment(loader=FileSystemLoader("terraform/registry/template"))
    template = env.get_template("registry.tfvars.j2")
    project_id = get_project_id()

    output_content = template.render(
        project_id=project_id,
        **HARD_CODED_VALUES,
    )

    tfvars_path = Path("terraform/registry/terraform.tfvars")
    with tfvars_path.open("w") as f:
        f.write(output_content)

    print(colored(f"Terraform configuration file generated: {tfvars_path}", "green"))
