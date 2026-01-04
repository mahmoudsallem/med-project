# ArgoCD Installation Guide

This guide provides step-by-step instructions for installing ArgoCD on your EKS cluster.

## Prerequisites

- A running Kubernetes/EKS cluster
- `kubectl` configured to access your cluster
- Cluster admin permissions
- Helm 3 installed ([Installation Guide](https://helm.sh/docs/intro/install/))

## Installation Steps

### 1. Add ArgoCD Helm Repository

```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
```

### 2. Create ArgoCD Namespace

```bash
kubectl create namespace argocd
```

### 3. Install ArgoCD using Helm

#### Basic Installation

```bash
helm install argocd argo/argo-cd -n argocd
```

#### Installation with Custom Values (Recommended)

Create a `argocd-values.yaml` file for customization:

```yaml
# argocd-values.yaml
server:
  service:
    type: LoadBalancer  # Change to ClusterIP if using Ingress
  
  ingress:
    enabled: false  # Set to true if using Ingress
    # ingressClassName: nginx
    # hosts:
    #   - argocd.yourdomain.com
    # annotations:
    #   cert-manager.io/cluster-issuer: letsencrypt-prod
    # tls:
    #   - secretName: argocd-tls
    #     hosts:
    #       - argocd.yourdomain.com

configs:
  params:
    server.insecure: true  # Set to false in production with TLS

# Optional: Enable HA mode
# redis-ha:
#   enabled: true
# controller:
#   replicas: 3
# server:
#   replicas: 3
# repoServer:
#   replicas: 3
```

Install with custom values:

```bash
helm install argocd argo/argo-cd -n argocd -f argocd-values.yaml
```

### 4. Verify Installation

Wait for all ArgoCD pods to be running:

```bash
kubectl get pods -n argocd
```

You should see pods like:
- `argocd-server`
- `argocd-repo-server`
- `argocd-application-controller`
- `argocd-dex-server`
- `argocd-redis`

### 4. Access ArgoCD UI

#### Option A: Port Forwarding (Quick Access)

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Then access ArgoCD at: `https://localhost:8080`

#### Option B: LoadBalancer (Production)

Change the `argocd-server` service type to LoadBalancer:

```bash
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
```

Get the external IP/hostname:

```bash
kubectl get svc argocd-server -n argocd
```

Wait for the `EXTERNAL-IP` to be assigned, then access ArgoCD using that address.

#### Option C: Ingress (Recommended for Production)

Create an Ingress resource for ArgoCD (requires an Ingress Controller like NGINX):

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: argocd-server-ingress
  namespace: argocd
  annotations:
    nginx.ingress.kubernetes.io/ssl-passthrough: "true"
    nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
spec:
  ingressClassName: nginx
  rules:
  - host: argocd.yourdomain.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: argocd-server
            port:
              number: 443
```

## Getting the Admin Password

### Retrieve Initial Admin Password

The initial admin password is auto-generated and stored in a Kubernetes secret.

**Method 1: Using kubectl (Recommended)**

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d && echo
```

**Method 2: Using argocd CLI**

First, install the ArgoCD CLI:

```bash
# Linux
curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
rm argocd-linux-amd64
```

Then get the password:

```bash
argocd admin initial-password -n argocd
```

### Login Credentials

- **Username**: `admin`
- **Password**: Use the password retrieved from the commands above

## Post-Installation Steps

### 1. Login via CLI

```bash
# If using port-forward
argocd login localhost:8080

# If using LoadBalancer or Ingress
argocd login <ARGOCD_SERVER_URL>
```

### 2. Change Admin Password (Recommended)

After first login, change the default password:

```bash
argocd account update-password
```

Or via UI: User Info → Update Password

### 3. Delete Initial Secret (Optional)

After changing the password, you can delete the initial secret:

```bash
kubectl -n argocd delete secret argocd-initial-admin-secret
```

## Installing ArgoCD CLI

### Linux

```bash
curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
rm argocd-linux-amd64
```

### macOS

```bash
brew install argocd
```

### Windows

Download from: https://github.com/argoproj/argo-cd/releases/latest

## Troubleshooting

### Pods Not Starting

Check pod status and logs:

```bash
kubectl get pods -n argocd
kubectl logs -n argocd <pod-name>
```

### Cannot Access UI

Verify the service is running:

```bash
kubectl get svc -n argocd argocd-server
```

Check if port-forward is active:

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

### Password Not Working

Ensure you're decoding the password correctly:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

## Managing ArgoCD with Helm

### Upgrade ArgoCD

Update to the latest version:

```bash
helm repo update
helm upgrade argocd argo/argo-cd -n argocd
```

Upgrade with custom values:

```bash
helm upgrade argocd argo/argo-cd -n argocd -f argocd-values.yaml
```

### Check Current Version

```bash
helm list -n argocd
```

### View ArgoCD Chart Values

See all configurable values:

```bash
helm show values argo/argo-cd
```

See your current values:

```bash
helm get values argocd -n argocd
```

### Rollback ArgoCD

If an upgrade causes issues:

```bash
helm rollback argocd -n argocd
```

## Uninstalling ArgoCD

To completely remove ArgoCD:

```bash
helm uninstall argocd -n argocd
kubectl delete namespace argocd
```

## Additional Resources

- [Official ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [ArgoCD GitHub Repository](https://github.com/argoproj/argo-cd)
- [ArgoCD Getting Started Guide](https://argo-cd.readthedocs.io/en/stable/getting_started/)

## Quick Reference Commands

```bash
# Get all ArgoCD resources
kubectl get all -n argocd

# Get ArgoCD server URL (if LoadBalancer)
kubectl get svc argocd-server -n argocd

# Get admin password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d && echo

# Port forward to access UI
kubectl port-forward svc/argocd-server -n argocd 8080:443

# Login via CLI
argocd login localhost:8080

# List applications
argocd app list

# Sync an application
argocd app sync <app-name>
```
