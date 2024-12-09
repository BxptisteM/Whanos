#!/bin/bash

ENV_FILE=".env"
if [ -f "$ENV_FILE" ]; then
    echo "Loading environment variables from $ENV_FILE..."
    export $(grep -v '^#' "$ENV_FILE" | xargs)
else
    echo "Error: $ENV_FILE file not found!"
    exit 1
fi

if [ -z "$SSH_USERNAME" ] || [ -z "$SSH_PRIVATE_KEY_PATH" ]; then
    echo "Error: SSH_USERNAME or SSH_PRIVATE_KEY_PATH not set in .env file."
    exit 1
fi

TERRAFORM_DIR="terraform/master"
ANSIBLE_DIR="ansible/roles/jenkins/files/deployment_pipeline"
REMOTE_PATH="/var/lib/jenkins/deployment_pipeline"

echo "Navigating to Terraform directory: $TERRAFORM_DIR"
cd "$TERRAFORM_DIR" || { echo "Directory not found: $TERRAFORM_DIR"; exit 1; }

echo "Fetching VM external IP from Terraform outputs..."
VM_EXTERNAL_IP=$(terraform output -raw vm_external_ip)
if [ -z "$VM_EXTERNAL_IP" ]; then
    echo "Failed to retrieve VM external IP. Exiting."
    exit 1
fi

echo "VM External IP: $VM_EXTERNAL_IP"

echo "Returning to base directory..."
cd - || exit 1

echo "Ensuring remote directory exists and is writable..."
ssh -i "$SSH_PRIVATE_KEY_PATH" "${SSH_USERNAME}@${VM_EXTERNAL_IP}" "sudo mkdir -p $REMOTE_PATH && sudo chown -R $SSH_USERNAME $REMOTE_PATH"
if [ $? -ne 0 ]; then
    echo "Failed to prepare remote directory. Exiting."
    exit 1
fi

echo "Uploading deployment_pipeline folder to the remote machine..."
scp -i "$SSH_PRIVATE_KEY_PATH" -r "$ANSIBLE_DIR"/* "${SSH_USERNAME}@${VM_EXTERNAL_IP}:${REMOTE_PATH}"
if [ $? -eq 0 ]; then
    echo "Upload successful!"
else
    echo "Failed to upload files. Please check your SSH connection and file paths."
    exit 1
fi
