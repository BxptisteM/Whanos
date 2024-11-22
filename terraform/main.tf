provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}


module "vpc" {
  source       = "./modules/network"
  network_name = "whanos-vpc"
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
    network = module.vpc.vpc_network

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

module "k8s_nodes" {
  region       = var.region
  source       = "./modules/compute"
  project_id   = var.project_id
  node_count   = 3
  machine_type = "e2-medium"
  disk_image   = "projects/debian-cloud/global/images/debian-12-bookworm-v20241112"
  network      = module.vpc.vpc_network
  ssh_keys     = var.ssh_keys
}
