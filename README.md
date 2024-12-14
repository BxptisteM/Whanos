
# Whanos 🚀⚙️🐳

![Project Banner](docs/assets/banner.png)

Welcome to the **Whanos Project**! This project is a DevOps powerhouse designed to automate the deployment of applications with ease and precision. Inspired by legendary tools, Whanos is the ultimate infrastructure to containerize, deploy, and manage applications in Kubernetes clusters, triggered by a simple Git push.

---

## 🎯 Objective

Create an automated pipeline that:

1. Fetches code from a Git repository.
2. Identifies the application technology.
3. Builds a container image.
4. Pushes the image to a Docker registry.
5. Deploys the application in a Kubernetes cluster.

---

## 🚀 Features

- **Multi-language Support**:
  - C, Java, JavaScript, Python, and Befunge.
- **End-to-end Automation**:
  - From code to container to deployment.
- **Customizable Deployment**:
  - Configurable replicas, resource limits, and ports via `whanos.yml`.

---

## 🛠️ Tech Stack

This project leverages a robust DevOps stack:

- **Python**: Utility scripts for automation ![Python Logo](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
- **Terraform**: Master machine and cluster creation ![Terraform Logo](https://img.shields.io/badge/Terraform-623CE4?logo=terraform&logoColor=white)
- **Ansible**: VM setup and configuration ![Ansible Logo](https://img.shields.io/badge/Ansible-EE0000?logo=ansible&logoColor=white)
- **Jenkins (JCasC + JobDSL)**: CI/CD pipeline and job management ![Jenkins Logo](https://img.shields.io/badge/Jenkins-D24939?logo=jenkins&logoColor=white)
- **GoogleCloud Registry**: Docker image registry ![Docker Logo](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
- **Helm**: Kubernetes application deployment and updates ![Helm Logo](https://img.shields.io/badge/Helm-0F1689?logo=helm&logoColor=white)


---

## 🌟 How It Works

1. **Setup your environment**:
   - Create a .env file (following the .env.example file) and fill it up with the asked variables
2. **Python Script**:
   - Use the `werserk.py` python script to initialize and deploy your infrastructure (see --help for more details).
3. **Terraform**:
   - Provisions the virtual machine for Jenkins and Kubernetes.
4. **Ansible**:
   - Configures the VM and ensures dependencies are installed.
5. **Jenkins (JCasC)**:
   - Automates Jenkins configuration.
6. **CI/CD Pipeline**:
   - Jobs created with JobDSL containerize and deploy applications.
7. **Helm**:
   - Updates Kubernetes pods with the latest Docker images.

---

## 📖 Documentation

All the detailed developper documentation can be found in the [Documentation](/docs/) folde.

---

## 🚀 Deployment Guide

### Prerequisites

- SSH key-pair for accessing your infrastructure.
- Python3, Pip, Ansible installed locally
- A valid GCP account

### Commands

- **Run Python script**: `python3 scripts/werserk.py --[FLAG]`
- **Deploy infrastructure**: Execute Terraform and Ansible steps outlined in `docs/TERRAFORM.md`.

---

## 🔗 Contributions

We welcome contributions! Please check out the [Contributing Guide](CONTRIBUTING.md) for setup instructions and contribution guidelines.

---

## ✨ Authors

- [Baptiste Moreau](https://github.com/BxptisteM)
- [Dragos Suceveanu](https://github.com/sdragos1)

--- 
