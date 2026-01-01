# Deploy Project Instructions

Follow these steps exactly to deploy the project on a new machine.

## 1. Setup Minikube (Fresh Start)
```bash
minikube start --driver=docker --cni=cilium #or calico (flannel can not work with network policies)
```
*Wait for it to finish.*

## 2. Set up Namespaces
```bash
kubectl create ns frontend-ns
kubectl label ns frontend-ns name=frontend-ns

kubectl create ns backend-ns
kubectl label ns backend-ns name=backend-ns

kubectl create ns db-ns
kubectl label ns db-ns name=db-ns
```

## 3. Enable Ingress Controller
```bash
minikube addons enable ingress
```

## 4. Deploy Application
Run these commands in order from the project root folder:

```bash
# 1. Database Layer (Wait for them to run before proceeding!)
kubectl apply -f k8s/db/

# 2. Backend Layer
kubectl apply -f k8s/backend/

# 3. Frontend Layer
kubectl apply -f k8s/frontend/

# 4. Network Policies (Security)
kubectl apply -f k8s/network-policies/
```

## 5. Configure Connectivity (Crucial Step)

### Get Minikube IP
```bash
minikube ip
```
*(Copy this IP, e.g., 192.168.49.2)*

### Patch Ingress for Access
Run this command, replacing `192.168.49.2` with YOUR Minikube IP from the step above:
```bash
kubectl patch svc ingress-nginx-controller -n ingress-nginx -p '{"spec":{"externalIPs":["192.168.49.2"]}}'
```

### Update Hosts File
Add these lines to your `/etc/hosts` file (or Windows hosts file), using the same IP:
```
192.168.49.2  frontend.nti.com
192.168.49.2  backend.nti.com
```

## 6. Access
Open in browser: `http://frontend.nti.com`
