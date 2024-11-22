output "vm_external_ip" {
  value = google_compute_instance.vm_instance.network_interface[0].access_config[0].nat_ip
}

output "k8s_node_ips" {
  value = module.k8s_nodes.node_ips
}
