from cli.args import get_args
from cli.setup.server_init import server_init
from cli.install.install import install

if __name__ == "__main__":
    args = get_args()
    if args.setup:
        server_init()
    if args.install:
        install()
