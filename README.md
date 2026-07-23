# High-Availability Serverless Container Microservice

## Why I Built This
Every other Lambda project in this portfolio uses zip-file deployment. I wanted to prove I 
understood the alternative: packaging Lambda as a container image via ECR. That's what teams 
reach for once dependencies exceed the 250MB unzipped limit, or when local dev needs to exactly 
match production.

## What I Built
- **Containerization:** Python 3.12 backend packaged in a Docker image built from AWS's official 
  `public.ecr.aws/lambda/python` base image, version-locking the runtime.
- **Registry:** Pushed to a private Amazon ECR repository.
- **Compute:** Lambda configured with package type `Image`, pointing directly at the ECR image 
  URI instead of a zip artifact.
- **Exposure:** API Gateway REST API with Lambda proxy integration, so the function receives the 
  full request object (headers, query params, body).

## What I'd Do Next
This proves the pattern works, but it's not hardened yet. Next: a `/health` route for liveness 
checking, a GitHub Actions workflow to auto-build and push the image to ECR on merge (same CI/CD 
pattern as my compliance monitor), and Trivy scanning against the base image layers before every 
push, so a known-CVE base image can't silently ship.
