resource "google_compute_address" "static_ips" {
  count  = var.node_count
  name   = "k8s-node-ip-${count.index}"
  region = var.region
}

resource "google_compute_instance" "k8s_nodes" {
  count                     = var.node_count
  name                      = "k8s-node-${count.index}"
  project                   = var.project_id
  machine_type              = var.machine_type
  allow_stopping_for_update = true

  boot_disk {
    initialize_params {
      image = var.disk_image
    }
  }

  network_interface {
    network = var.network
    access_config {
      nat_ip = google_compute_address.static_ips[count.index].address
    }
  }

  scheduling {
    automatic_restart   = true
    on_host_maintenance = "MIGRATE"
    provisioning_model  = "STANDARD"
  }

  shielded_instance_config {
    enable_secure_boot          = false
    enable_vtpm                 = true
    enable_integrity_monitoring = true
  }

  metadata = {
    ssh-keys = var.ssh_keys
  }
}
