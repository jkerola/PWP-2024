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

# Usage

Easiest way to get this up and running is to use podman/docker:

```shell
# create .env file in the root directory
touch .env
# fill in the details as such
DB_PASSWORD=<username>
DB_USER=<password>

podman-compose up -d
# Or docker
docker compose up -d

# then make requests to localhost:3000
curl -X GET localhost:3000
```

# Examine database contents with adminer

Navigate to [http://localhost:8080](http://localhost:8080) and login with the above details. Server should be _'db'_ and database should be _'postgres'_.
