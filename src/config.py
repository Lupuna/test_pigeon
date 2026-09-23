import os
from datetime import timezone

DBNAME = os.getenv("POSTGRES_DB", "dbname")
DBUSER = os.getenv("POSTGRES_USER", "dbuser")
PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DBHOST = os.getenv("POSTGRES_HOST", "localhost")

DATABASE_URL = f"postgresql+asyncpg://{DBUSER}:{PASSWORD}@{DBHOST}:5432/{DBNAME}"
TIMEZONE = timezone.utc
