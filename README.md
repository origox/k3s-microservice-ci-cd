# k3s-microservice-ci-cd/k3s-microservice-ci-cd-helm-charts
Development of a python micro service running in a kubernetes cluster backed by best GitOps practices 

My current focus is to get a ci/cd pipeline up&running. The actaul app is secondary and will for now be a hello world-ish app.

# Devolopment Structure

## Workflow
dev app code => ci/cd pipeline will tests app, build app container, deliver to dockerhub, update helm charts => Fleet will deploy newly releases container

## Frameworks/Technologies
- FastAPI - Fast and robust Python Web/API framework
- MongoDB - NoSQL database
- Motor - Non-blocking API for MongoDB
- Uvicorn - ASGI web server
- GitHub Actions workflows for CI/CD pipeline
- Docker/Dockerhub - Containerize everything
- K3S - Kubernetes
- Fleet from Suse/Rancher - Continous Deployment to my K3S cluster 

## Repositories

### origox/k3s-microservice-ci-cd
- Github repo for actual app source, dockerfile and gitops workflow(CI and Continous Delivery) i.e. this repo

### origox/k3s-microservice-ci-cd-helm-charts 
- [origox/k3s-microservice-ci-cd-helm-charts](https://github.com/origox/k3s-microservice-ci-cd-helm-charts)
- Related Github repo holding Helm charts for app deployment.
- This repo will be related to Fleet i.e. "container management and deployment engine"

### GHCR - Container Registry
- https://github.com/origox/k3s-microservice-ci-cd/pkgs/container/k3s-microservice-ci-cd


## Rancher/Suse Fleet Setup

# Future ideas
- Develop an AI/ML api
- Separate web html from actual Api service 
- Messagebus, Celery, ...

