provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

resource "google_compute_instance" "vm_instance" {
  name         = var.vm_name
  machine_type = var.machine_type
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = var.image
      type  = var.disk_type
      size  = var.disk_size
    }
  }

  network_interface {
    subnetwork = "default"

    access_config {
      network_tier = "PREMIUM"
    }
  }

  metadata = {
    ssh-keys = var.ssh_keys
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
}


output "vm_external_ip" {
  value = google_compute_instance.vm_instance.network_interface[0].access_config[0].nat_ip
}

variable "project_id" {}
variable "region" {}
variable "zone" {}
variable "vm_name" {}
variable "machine_type" {}
variable "image" {}
variable "disk_type" {}
variable "disk_size" {
  type = number
}
variable "ssh_keys" {}
