
# Study on Technological Choices for the Whanos Project

## Terraform

### Features:
- **Ease of Integration**: Integrates seamlessly with GCP by providing configuration files.
- **Automation**: Reduces manual actions required during VM creation.
- **Infrastructure Management**: Enables infrastructure definition and management via configuration files, ensuring reproducibility and facilitating updates.
- **Efficiency**: Enhances speed and efficiency in virtual machine deployment.
- **Team Collaboration**: Promotes teamwork by allowing all team members to deploy identical environments quickly.
- **Simplified Operations**: Provides simple resource creation and deletion processes.

**Why Terraform was chosen:**
Terraform stands out for its reliability, automation capabilities, and ability to ensure infrastructure reproducibility. Its integration with GCP and support for team collaboration make it an ideal choice for VM provisioning.

---

## Docker Hub

### Features:
- **CLI Integration**: Integrated with the Docker CLI, enabling easy use with commands like `docker pull` and `docker push`.
- **Web Interface**: Provides a user-friendly interface for managing and visualizing Docker images.
- **Cost-Effective**: Free to use within certain limits.
- **Documentation**: Offers extensive documentation to simplify usage.
- **Standardization**: Widely recognized as the standard registry for Docker images.

**Why Docker Hub was chosen:**
Docker Hub was selected for its ease of use, standardization, and excellent tooling, making it a reliable choice for managing container images in the project.

---

## Ansible

### Features:
- **Proven Experience**: Familiar tool with prior usage experience in similar projects.
- **Industry Adoption**: Widely adopted across organizations for configuration management.
- **Compatibility**: Integrates seamlessly with Terraform for provisioning workflows.
- **Connection Simplicity**: Operates using only SSH for VM updates.
- **Consistency**: Ensures consistent configurations across VMs.
- **Scalability**: Allows easy updates and management for growing infrastructures.
- **Automation**: Reduces manual errors and improves standardization.

**Why Ansible was chosen:**
Ansible’s compatibility with Terraform, focus on automation, and scalability made it an excellent choice for configuring VMs. Its industry adoption and simplicity further supported this decision.

---

## Helm

### Features:
- **Version Control**: Supports versioned deployments using Helm charts.
- **Kubernetes Native**: Fully integrates with Kubernetes, avoiding external tools.
- **Flexibility**: Enables use beyond pod updates, offering broader use-case coverage.
- **Ease of Use**: Simplifies application management and updates compared to alternatives.

### Considered Alternatives:
- **Cron Jobs and Scripts**: Faced scalability issues and required ongoing maintenance.
- **Watchtower**: Suitable for testing but not ideal for production environments.
- **ArgoCD/FluxCD**: Highly capable but overly complex to set up for this project’s requirements.

**Why Helm was chosen:**
Helm was selected for its Kubernetes-native approach, flexibility, and ability to manage versioned deployments efficiently, making it a robust solution for pod updates.

---

## Terraform and Kubespray for Kubernetes Cluster Setup

### Features:
- **Terraform**:
  - Provisions infrastructure flexibly across cloud, hybrid, or on-prem environments.
  - Manages complex networking setups and ensures consistent deployments using modules and state files.

- **Kubespray**:
  - Highly configurable for specific Kubernetes needs, including networking plugins and control plane configurations.
  - Customizable for monitoring, logging, and storage solutions tailored to project requirements.

**Why Terraform and Kubespray were chosen:**
This combination leverages Terraform’s flexibility for infrastructure provisioning and Kubespray’s fine-grained control for Kubernetes setup, delivering an optimal solution for cluster management.

---
