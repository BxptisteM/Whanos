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
