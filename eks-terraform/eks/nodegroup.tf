resource "aws_eks_node_group" "private" {
  cluster_name    = aws_eks_cluster.this.name
  node_group_name = "private-ng"
  node_role_arn   = aws_iam_role.eks_nodes.arn
  subnet_ids      = var.private_subnets

  scaling_config {
    desired_size = 2
    max_size     = 4
    min_size     = 1
  }

  instance_types = ["t3.medium"]

  # Enable remote access for troubleshooting (optional, remove if not needed)
  # remote_access {
  #   ec2_ssh_key = var.ssh_key_name
  #   source_security_group_ids = [aws_security_group.nodes.id]
  # }

  tags = {
    Name = "${var.cluster_name}-private-ng"
  }

  # Ensure IAM policies are attached before creating node group
  depends_on = [
    aws_iam_role_policy_attachment.worker_node,
    aws_iam_role_policy_attachment.cni,
    aws_iam_role_policy_attachment.ecr,
  ]
}

