resource "google_compute_network" "vpc" {
  name                    = "${var.project_id}-vpc"
  auto_create_subnetworks = "false"
}

resource "google_compute_subnetwork" "subnet" {
  name          = "${var.project_id}-subnet"
  region        = var.region
  network       = google_compute_network.vpc.name
  ip_cidr_range = "10.10.0.0/24"
}

resource "google_compute_firewall" "vpc_firewall_ssh" {
  name          = "vpc-firewall-ssh"
  network       = google_compute_network.vpc.name
  target_tags   = ["whanos-vm"]
  source_ranges = ["0.0.0.0/0"]

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
}

resource "google_compute_firewall" "vpc_firewall_http" {
  name          = "vpc-firewall-jenkins"
  network       = google_compute_network.vpc.name
  target_tags   = ["jenkins-vm"]
  source_ranges = ["0.0.0.0/0"]

  allow {
    protocol = "tcp"
    ports    = ["8080"]
  }
}

resource "google_compute_firewall" "vpc_firewall_outbound" {
  name    = "allow-outbound"
  network = google_compute_network.vpc.name

  allow {
    protocol = "tcp"
    ports    = ["443"]
  }

  destination_ranges = ["0.0.0.0/0"]
  direction          = "EGRESS"
}
