resource "google_compute_network" "vpc" {
  name = var.network_name
}

resource "google_compute_firewall" "vpc_firewall_ssh" {
  name          = "vpc-firewall-ssh"
  network       = google_compute_network.vpc.name
  source_ranges = ["0.0.0.0/0"]

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
  source_tags = ["whanos-master"]
}
