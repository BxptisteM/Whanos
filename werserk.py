from cli.args import get_args
from cli.setup.server_init import server_init
from cli.install.install import install
from cli.cluster.cluster import cluster
from cli.jenkins.jenkins import jenkins
from cli.registry.registry import registry

if __name__ == "__main__":
    args = get_args()
    if args.setup:
        server_init()
    if args.install:
        install()
    if args.cluster:
        cluster()
    if args.jenkins:
        jenkins()
    if args.registry:
        registry()
