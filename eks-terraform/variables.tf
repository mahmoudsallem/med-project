variable "aws_region" {
  default = "eu-central-1"
}

variable "cluster_name" {
  default = "devops-eks"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "public_subnets" {
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnets" {
  default = ["10.0.101.0/24", "10.0.102.0/24"]
}

variable "allowed_public_ip" {
  description = "Your IP for EKS API access"
}
