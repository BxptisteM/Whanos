resource "google_compute_instance" "k8s_nodes" {
  count        = var.node_count
  name         = "k8s-node-${count.index}"
  project      = var.project_id
  machine_type = var.machine_type

  boot_disk {
    initialize_params {
      image = var.disk_image
    }
  }

  network_interface {
    network = var.network
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
