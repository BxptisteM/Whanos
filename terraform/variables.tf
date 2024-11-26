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

variable "node_count" {
  type        = number
  description = "Number of nodes to create in the K8S cluster"
  default     = 2
}
