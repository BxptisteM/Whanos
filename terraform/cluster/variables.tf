variable "node_count" {
  type        = number
  description = "Number of nodes to create in the K8S cluster"
  default     = 2
}

variable "project_id" {
  description = "The project ID to deploy to"
  type        = string
}

variable "region" {
  description = "The region to deploy to"
  type        = string
}

variable "vpc_name" {
  description = "The name of the created VPC network"
  type        = string
}

variable "subnet_name" {
  description = "The name of the created subnet"
  type        = string
}

variable "zone" {
  description = "The zone to deploy to"
  type        = string
}
