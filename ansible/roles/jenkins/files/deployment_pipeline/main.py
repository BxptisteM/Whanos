#!/usr/bin/env python3

from args import get_args
from deploy import deploy


if __name__ == "__main__":
    args = get_args()
    deploy(args.project)
