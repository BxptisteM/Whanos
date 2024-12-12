resource "google_artifact_registry_repository" "docker-repository" {
  location      = var.region
  repository_id = "${var.project_id}-docker-repository"
  description   = "Docker repository for storing Docker images"
  format        = "DOCKER"
  mode          = "STANDARD_REPOSITORY"
  project       = var.project_id

  docker_config {
    immutable_tags = false
  }
}
