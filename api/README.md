# Flask API

## Setup

```sh
# create a virtualenv
python3 -m venv venv
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

# Run the application with
flask run
```

Make sure a database is running by executing `docker compose up -d database` or `podman-compose up -d database` in the project root directory.
