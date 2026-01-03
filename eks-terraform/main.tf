module "vpc" {
  source          = "./vpc"
  cluster_name    = var.cluster_name
  vpc_cidr        = var.vpc_cidr
  public_subnets  = var.public_subnets
  private_subnets = var.private_subnets
}

module "eks" {
  source            = "./eks"
  cluster_name      = var.cluster_name
  vpc_id            = module.vpc.vpc_id
  private_subnets   = module.vpc.private_subnets
  public_subnets    = module.vpc.public_subnets
  allowed_public_ip = var.allowed_public_ip
}
