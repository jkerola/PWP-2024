# Flask API

## Setup

Create a .env file in the _api_ directory and fill it with the following, replacing < things > with whatever:

```shell
API_USERNAME=<username>
API_PASSWORD=<password>
SECRET_TOKEN=<secret string>
DB_PASSWORD=<username>
DB_USER=<password>
DATABASE_URL=postgresql://${DB_USER}:${DB_PASSWORD}@localhost:5432/db?schema=public
```

Make sure a database is running by executing `docker compose up -d database` or `podman-compose up -d database` in the project root directory.

Run the application with:

```sh
# create a virtualenv
python3 -m venv venv
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

# Create tables
prisma generate
prisma db push

# Run the application with
flask run
```
