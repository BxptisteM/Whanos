from jinja2 import Environment, FileSystemLoader
from termcolor import colored
from pathlib import Path
import subprocess
from cli.utils.project_id import get_project_id

HARD_CODED_VALUES = {
    "region": "europe-west1",
    "node_count": 1,
    "zone": "europe-west1-d",
}


def get_vpc_name():
    terraform_dir = Path("terraform/master")
    result = subprocess.run(
        ["terraform", "output", "-raw", "vpc_name"],
        check=True,
        text=True,
        capture_output=True,
        cwd=terraform_dir,
    )
    return result.stdout.strip()


def get_subnet_name():
    terraform_dir = Path("terraform/master")
    result = subprocess.run(
        ["terraform", "output", "-raw", "subnet_name"],
        check=True,
        text=True,
        capture_output=True,
        cwd=terraform_dir,
    )
    return result.stdout.strip()


def terraform_generate_cluster_tfvars():
    env = Environment(loader=FileSystemLoader("terraform/cluster/template"))
    template = env.get_template("cluster.tfvars.j2")
    project_id = get_project_id()

    output_content = template.render(
        project_id=project_id,
        **HARD_CODED_VALUES,
        vpc_name=get_vpc_name(),
        subnet_name=get_subnet_name(),
    )

    tfvars_path = Path("terraform/cluster/terraform.tfvars")
    with tfvars_path.open("w") as f:
        f.write(output_content)

    print(colored(f"Terraform configuration file generated: {tfvars_path}", "green"))
