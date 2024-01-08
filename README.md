# PWP SPRING 2024

# PROJECT NAME

# Group information

- Student 1. Janne Kerola janne.kerola@oulu.fi
- Student 2. Name and email
- Student 3. Name and email
- Student 4. Name and email

**Remember to include all required documentation and HOWTOs, including how to create and populate the database, how to run and test the API, the url to the entrypoint and instructions on how to setup and run the client**

# Pre-commit

We use [pre-commit](https://pre-commit.com) to ensure code quality.

```shell
# Install pre-commit with pip
pip3 install pre-commit
# Run this to initialize pre-commit in the repo
cd /path/to/repo
pre-commit install
```

# Development

API is build with [nestjs](nestjs.com). Node version 20/LTS required.

# Usage

Easiest way to get this up and running is to use podman/docker:

```shell
podman-compose up -d
# Or docker
docker compose up -d

# then make requests to localhost:3000
curl -X GET localhost:3000
```
