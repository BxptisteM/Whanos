import argparse


def get_args() -> argparse.Namespace:
    parser = parser = argparse.ArgumentParser(
        description="Deployment pipeline arguments"
    )
    parser.add_argument(
        "--project",
        type=str,
        required=True,
        help="Project name",
    )
    return parser.parse_args()
