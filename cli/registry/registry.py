from termcolor import colored
from cli.registry.vars import terraform_generate_registry_tfvars
from cli.registry.resources import generate_registry_resource


def registry():
    print(colored("Creating Docker registry...", "yellow"))
    terraform_generate_registry_tfvars()
    generate_registry_resource()
    print(colored("Docker registry created!", "green"))
