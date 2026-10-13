# Flask Shop

Flask backend for the shop application.

## Setup

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```powershell
uv sync
$env:MYSQL_HOST = "127.0.0.1"
$env:MYSQL_PORT = "3306"
$env:MYSQL_DATABASE = "flask_shop"
$env:MYSQL_USERNAME = "root"
$env:MYSQL_PASSWORD = "your-local-database-password"
$env:SECRET_KEY = "set-a-private-random-value"
uv run python manager.py
```

Set `MYSQL_PASSWORD` and `SECRET_KEY` in the environment for your own machine. The built-in secret key is only a development placeholder; use a private random value for any deployment.
