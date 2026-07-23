# High-Availability Serverless Container Microservice

## Business Case
Traditional Lambda deployments are limited by a 250MB unzipped package size, which becomes 
a real constraint once you need larger dependencies (ML libraries, complex SDKs, custom binaries). 
Enterprises increasingly package Lambda functions as container images (via ECR) instead of zip 
uploads specifically to escape this limit while keeping the operational simplicity of serverless — 
no servers to patch, scale, or manage. This project proves that container-based Lambda deployment 
pattern end-to-end.

## Architecture
- **Containerization:** Python backend packaged in a Docker image using the AWS base Lambda image, 
  ensuring the exact runtime environment is version-locked and reproducible.
- **Registry:** Image pushed to Amazon ECR (Elastic Container Registry).
- **Compute:** AWS Lambda configured to pull its runtime directly from the ECR image rather than a 
  zip artifact.
- **Exposure:** Fronted by API Gateway for secure, throttled HTTP access.

## Why Container Images Over Zip Packaging
- Removes the 250MB unzipped deployment size ceiling.
- Enables consistent local-to-cloud testing — the same image that runs in Lambda can be run and 
  debugged locally via Docker.
- Better dependency isolation, since the full OS-level environment is defined in the Dockerfile 
  rather than assembled at deploy time.

## Current Scope & Next Steps
This is a v1 proof of the deployment pattern. Planned next:
- Add a health-check endpoint and basic structured logging.
- Wire up a GitHub Actions pipeline to auto-build and push the image to ECR on merge (extending the 
  same DevSecOps pattern used in the compliance monitor project).
- Add Checkov/container image scanning (e.g., Trivy) to catch vulnerable base image layers before push.
<img width="1350" height="645" alt="AWS - Microservice Success Test" src="https://github.com/user-attachments/assets/008f1a0a-e11b-4b68-8c38-1d256dd22b42" />
# serverless-container-microservice
High-availability Python backend packaged in a Docker container and deployed via AWS ECR and Lambda.
