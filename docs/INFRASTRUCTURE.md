# Infrastructure Overview

This document explains how the infrastructure is set up and operates.

## Overview of Infrastructure Components

1. **Terraform**
   - Terraform is the foundational building block, used to provision the following resources:
     - A master VM
     - A Kubernetes cluster
     - VPCs (Virtual Private Clouds)
     - A Docker registry

2. **Ansible**
   - Ansible playbooks are executed to prepare the master VM by performing these tasks:
     - Setting up Jenkins and its configurations
     - Installing dependencies such as Kubectl, Gcloud, Docker, etc.
     - Transferring necessary files to the master VM, including Kubernetes manifests and Dockerfiles

3. **Jenkins Pipeline**
   - Jenkins automates building, pushing, and deploying Docker images using the following steps:
     1. A Git push triggers the Jenkins pipeline.
     2. The pipeline runs a deployment script located at `/ansible/roles/jenkins/files/deployment_pipeline`.
     3. The script performs the following actions:
        - Detects the language of the repository.
        - Determines if the repository is for a standalone or base Docker image.
        - Builds the appropriate Docker image.
        - Pushes the image to the Docker registry.
        - Checks for a `whanos.yml` file in the repository root. If found, the image is deployed to the Kubernetes cluster.
        - Uses Helm to install the image into the cluster. If a deployment already exists, it performs a rolling update to upgrade it.

By combining these components, the infrastructure ensures automated provisioning, configuration, and deployment of applications to the Kubernetes cluster.
