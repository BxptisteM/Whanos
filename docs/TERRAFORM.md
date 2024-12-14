# Terraform Configuration Documentation

This document provides an overview of how Terraform is used to provision and configure a virtual machine (VM) in Google Cloud Platform (GCP) as part of the Whanos project.

---

## Overview

Terraform is leveraged to automate the creation of a GCP VM, utilizing a structured and modular approach. The Terraform configuration includes:
- A `main.tf` file defining the resources to be provisioned.
- A templated `terraform.tfvars` file for dynamic configuration based on user input and hardcoded values.
- A Python script to automate authentication, variable generation, and the Terraform workflow.

---

## Terraform Files

### `terraform.tfvars.j2`

This is a Jinja2 template used to dynamically generate the `terraform.tfvars` file. It accepts user inputs and hardcoded values, providing flexibility for customizing the VM.

**Template Structure:**
```hcl
project_id = "{{ project_id }}"
region     = "{{ region }}"
zone       = "{{ zone }}"
vm_name    = "{{ vm_name }}"
machine_type = "{{ machine_type }}"
image       = "{{ image }}"
disk_type   = "{{ disk_type }}"
disk_size   = {{ disk_size }}
ssh_keys    = "{{ ssh_keys }}"
```

### `main.tf`

The `main.tf` file defines the Google Cloud resources to be provisioned.

**Key Components:**
- **Provider Configuration:**
  ```hcl
  provider "google" {
    project = var.project_id
    region  = var.region
    zone    = var.zone
  }
  ```
  Specifies the GCP project, region, and zone.

- **Resource Definition:**
  ```hcl
  resource "google_compute_instance" "vm_instance" {
    name         = var.vm_name
    machine_type = var.machine_type
    zone         = var.zone
    ...
  }
  ```
  Provisions a compute instance with customizable attributes such as machine type, boot disk, and network configuration.

- **Output Configuration:**
  ```hcl
  output "vm_external_ip" {
    value = google_compute_instance.vm_instance.network_interface[0].access_config[0].nat_ip
  }
  ```
  Outputs the external IP address of the VM.

---

## Python Automation Script

The **server_init** Python script automates several steps in the Terraform workflow:
1. Authenticates the user with GCP.
2. Configures the GCP project based on user input.
3. Generates the `terraform.tfvars` file using the Jinja2 template.
4. Executes Terraform commands (`init` and `apply`) to deploy the infrastructure.
5. Retrieves the external IP of the VM post-deployment.
---

## Deployment Process

1. **Configure Environment Variables:**
   - Define `SSH_PUBLIC_KEY_PATH` and `SSH_USERNAME` in the `.env` file.

2. **Run the Python Script:**
   Execute the `werserk.py --setup` script:
   ```bash
   python3 werserk.py --setup
   ```

3. **Follow Authentication Steps:**
   Authenticate with Google Cloud as prompted.

4. **Provision the VM:**
   - The script will generate the `terraform.tfvars` file.
   - Terraform initializes and applies the configuration.
   - The VM's external IP will be displayed upon successful deployment.

---

## Notes

- The Terraform configuration enforces best practices such as:
  - Explicit variable declarations for flexibility.
  - Output configurations for retrieving deployment details.
  - Secure handling of SSH keys.

- Ensure that the GCP project is correctly set up with appropriate permissions before deployment.

---

## Troubleshooting

- **Authentication Issues:**
  Ensure the `gcloud` CLI is installed and correctly configured.

- **Terraform Errors:**
  Check the `terraform` logs for detailed error messages. Ensure all required variables are defined in the `terraform.tfvars` file.

- **SSH Connectivity:**
  Verify that the SSH key is properly configured and matches the `SSH_USERNAME` provided.

For further assistance, refer to the Terraform documentation or contact the project maintainers.
