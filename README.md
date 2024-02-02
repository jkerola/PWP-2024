# PWP SPRING 2024

# PROJECT NAME

# Group information

- Student 1. Janne Kerola janne.kerola@oulu.fi
- Student 2. Janne Tahkola janne.tahkola@oulu.fi
- Student 3. Emilia Pyyny epyyny20@student.oulu.fi
- Student 4. Errafay Amine aerrafay19@student.oulu.fi

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

This repository is a monorepo, containing all needed components for the course.

API directory contains the flask backend.

Create a .env file in the project root directory and fill it with the following, replacing < things > with whatever:

```shell
API_USERNAME=<username>
API_PASSWORD=<password>
SECRET_TOKEN=<secret string>
DB_PASSWORD=<username>
DB_USER=<password>
DB_NAME=<database name>
DATABASE_URL=postgresql://${DB_USER}:${DB_PASSWORD}@localhost:5432/${DB_NAME}?schema=public
```

# Usage

Easiest way to get this up and running is to use podman/docker:

```shell
podman-compose up -d
# Or docker
docker compose up -d

# then make requests to localhost:3000
curl -X GET localhost:3000
```
