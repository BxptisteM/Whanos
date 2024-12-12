#!/usr/bin/env python3

from args import get_args
from deploy import deploy
from gcloud import gcloud_auth


if __name__ == "__main__":
    args = get_args()
    gcloud_auth()
    deploy(args.project)
