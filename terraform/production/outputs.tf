output "render_project_id" {
  description = "The project ID for the Repalis Render project. Used for the render_project data source."
  value       = render_project.repalis.id
}

output "sandbox_environment_id" {
  description = "The Sandbox environment ID within the Repalis project."
  value       = render_project.repalis.environments["Sandbox"].id
}

output "test_environment_id" {
  description = "The Test environment ID within the Repalis project."
  value       = render_project.repalis.environments["Test"].id
}

output "redis_endpoint_service_name" {
  description = "VPC endpoint service name for the worker Redis. Provide to Render when creating the private link."
  value       = module.redis_private_link.service_name
}

output "grafana_cloudwatch_role_arn" {
  description = "IAM role ARN to provide in the Grafana Cloud CloudWatch scrape setup."
  value       = module.grafana_cloudwatch_role.role_arn
}

output "planetscale" {
  description = "PlanetScale production branch and application role."
  value       = module.planetscale
}
