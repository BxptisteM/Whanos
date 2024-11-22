variable "node_count" {
  type        = number
  description = "Number of nodes to create in the K8S cluster"
  default     = 2
}

variable "project_id" {
  type        = string
  description = "The project ID to deploy resources"
}

variable "machine_type" {
  type        = string
  description = "The machine type to use for the instances"
  default     = "e2-medium"
}

variable "disk_image" {
  type        = string
  description = "The image to use for the instances"
  default     = "projects/debian-cloud/global/images/debian-12-bookworm-v20241112"
}

variable "network" {
  type        = string
  description = "The network to use for the instances"
  default     = "default"
}

variable "ssh_keys" {
  type        = string
  description = "The SSH keys to add to the instances"
}

variable "region" {
  description = "The region to create the network in"
  type        = string
}
