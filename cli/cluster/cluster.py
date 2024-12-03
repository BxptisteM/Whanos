from termcolor import colored
from cli.cluster.vars import terraform_generate_cluster_tfvars
from cli.cluster.kubectl import configure_kubectl
from cli.cluster.resources import generate_cluster_resources


def cluster() -> None:
    print(colored("Creating your cluster...", "cyan"))
    terraform_generate_cluster_tfvars()
    generate_cluster_resources()
    configure_kubectl()
