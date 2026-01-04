# EKS Terraform Project

This repository contains Terraform configurations to provision a production-ready Amazon EKS (Elastic Kubernetes Service) cluster within a custom VPC, including an NGINX Ingress Controller.

## Architecture

![alt text](<WhatsApp Image 2026-01-04 at 10.45.40 AM.jpeg>)


The infrastructure is designed with security and scalability in mind, featuring:
- A custom VPC with public and private subnets across multiple Availability Zones.
- Private EKS Node Groups for enhanced security.
- Managed NAT Gateway for outbound internet access from private nodes.
- NGINX Ingress Controller for traffic management.

---

## Project Structure

The project is organized into modular components:

- **`vpc/`**: Manages networking infrastructure (VPC, Subnets, NAT Gateway, Routes).
- **`eks/`**: Provisions the EKS Cluster, IAM roles, and Managed Node Groups.
- **`ingress/`**: Deploys the NGINX Ingress Controller using Helm.
- **Root Files**:
  - `main.tf`: Coordinates the deployment of modules.
  - `variables.tf` & `terraform.tfvars`: Configuration for region, CIDRs, and cluster naming.
  - `provider.tf`: Configuration for AWS, Kubernetes, and Helm providers.

---

## Resources Created

### Networking (VPC Module)
- **VPC**: `10.0.0.0/16` (default) with DNS support and hostnames enabled.
- **Public Subnets**: Used for the NAT Gateway and Load Balancers.
- **Private Subnets**: Where the EKS worker nodes reside.
- **NAT Gateway**: Enables internet access for resources in private subnets.
- **Internet Gateway**: Provides connectivity for public subnets.

### Compute (EKS Module)
- **EKS Cluster**: Highly available managed Kubernetes control plane.
- **Managed Node Group**: 
  - Instance Type: `t3.medium`
  - Scaling: Min 1, Max 4, Desired 2.
  - Deployment: Private subnets.
- **IAM Roles**: Least-privilege roles for the EKS Cluster and Node Groups.

### Ingress (Ingress Module)
- **Namespace**: `ingress-nginx`
- **Controller**: NGINX Ingress Controller deployed via Helm release.
- **Service**: LoadBalancer type to expose the ingress to the internet.

---

## Getting Started

### Prerequisites
- [AWS CLI](https://aws.amazon.com/cli/) configured with appropriate credentials.
- [Terraform](https://www.terraform.io/downloads) (>= 1.5.0)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/docs/intro/install/)

### Deployment

1. **Initialize Terraform**:
   ```bash
   terraform init
   ```

2. **See the Execution Plan**:
   ```bash
   terraform plan
   ```

3. **Apply the Configuration**:
   ```bash
   terraform apply
   ```

4. **Update Kubeconfig**:
   After deployment, update your local kubeconfig to connect to the cluster:
   ```bash
   aws eks update-kubeconfig --region <your-region> --name <cluster-name>
   ```

### Cleanup
To destroy the provisioned infrastructure:
```bash
terraform destroy
```

---

## Note on Ingress Module
> [!NOTE]  
> The `ingress` module is available in the `ingress/` directory but is intended to be called after the EKS cluster is fully operational and the Kubernetes provider is configured with the cluster credentials.
