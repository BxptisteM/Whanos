output "node_ips" {
  value = [for ip in google_compute_address.static_ips : ip.address]
}
