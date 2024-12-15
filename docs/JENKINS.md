# Jenkins Configuration and Available Jobs

## Overview
This documentation provides an overview of the Jenkins configuration, including the structure of jobs and folders, and the Job DSL scripts used for job creation.

---

## Job DSL Files
### `projects.groovy`
This script defines a folder named **Projects** and a job called **link-project**.

#### Folder: Projects
- **Description:** Contains all project-specific jobs.

#### Job: link-project
- **Description:** Links a specified project to Jenkins by creating a job under the **Projects** folder.
- **Parameters:**
  - `PROJECT_NAME` (string): The name of the project.
  - `REPO_SSH_URL` (string): SSH URL of the repository.
  - `DEPLOY_KEY` (credentials): SSH key for deploying build artifacts.
  - `BRANCH` (choice): Branch to check out (`main`, `master`, `develop`).

- **Steps:**
  - Creates a freestyle job for the specified project.
  - Configures Git SCM with the repository and branch.
  - Schedules a periodic SCM trigger (`* * * * *`).
  - Executes a deployment script located at `/var/lib/jenkins/deployment_pipeline/main.py`.

---

### `whanos_images.groovy`
This script defines a folder named **Whanos base images** and various jobs to build Docker base images.

#### Folder: Whanos base images
- **Description:** Contains jobs related to building Docker base images.

#### Job: Build all base images
- **Description:** Builds all base Docker images simultaneously.
- **Steps:**
  - Runs Docker build commands for all supported languages (`c`, `python`, `java`, `javascript`, `befunge`).

#### Language-Specific Jobs
- **Description:** Builds Docker base images for individual languages.
- **Steps:**
  - Defines a freestyle job for each language.
  - Executes a Docker build command using the relevant Dockerfile (`Dockerfile.base`).

---

## Additional Notes
- **Job Persistence:**
  - Jobs keep logs and artifacts for a limited number of builds (2-4 builds).
- **Security Considerations:**
  - Ensure credentials are securely managed.
- **Future Improvements:**
  - Consider adding email notifications for build failures.
  - Implement build promotion and testing stages.

