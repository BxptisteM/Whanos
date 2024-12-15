provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

resource "google_project_service" "k8s" {
  service            = "container.googleapis.com"
  disable_on_destroy = false
}

data "google_container_engine_versions" "gke_version" {
  location       = var.region
  version_prefix = "1.27."
}

resource "google_container_cluster" "primary" {
  name     = "${var.project_id}-gke"
  location = var.region

  remove_default_node_pool = true
  initial_node_count       = 1

  network    = var.vpc_name
  subnetwork = var.subnet_name

  node_config {
    disk_size_gb = 50
  }

  release_channel {
    channel = "STABLE"
  }
}

resource "google_container_node_pool" "primary_nodes" {
  name     = "${google_container_cluster.primary.name}-node-pool"
  location = var.region
  cluster  = google_container_cluster.primary.name

  node_count = var.node_count

  node_config {
    oauth_scopes = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
      "https://www.googleapis.com/auth/cloud-platform",
      "https://www.googleapis.com/auth/devstorage.read_only",
      "https://www.googleapis.com/auth/servicecontrol",
      "https://www.googleapis.com/auth/service.management.readonly",
      "https://www.googleapis.com/auth/trace.append"
    ]
    disk_size_gb = 20
    labels = {
      env = var.project_id
    }

    service_account = "jenkins-sa@${var.project_id}.iam.gserviceaccount.com"
    machine_type = "e2-small"
    tags         = ["gke-node", "${var.project_id}-gke", "whanos-vm"]
    metadata = {
      disable-legacy-endpoints = "true"
    }
  }
}
