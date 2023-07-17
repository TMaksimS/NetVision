from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres_test:postgres_test@0.0.0.0:5432/postgres_test")

APP_URL = env.str(
    "APP_URL",
    default="http://0.0.0.0:8000"
)

