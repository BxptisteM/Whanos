import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="berserkcli",
        description="CLI for the Whanos Project",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1",
    )
    parser.add_argument(
        "--setup",
        help="Setup cloud provider as well as terraform resources",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--install",
        help="Install the dependencies needed for the infrastructure",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--cluster",
        help="Setup the kubernetes cluster",
        default=False,
        action="store_true",
    )
    return parser.parse_args()
