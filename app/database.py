from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from collections.abc import Iterator
from sqlalchemy.orm import Session

from app.config import Settings

settings = Settings()

database_url = URL.create(
    drivername="postgresql+psycopg",
    username=settings.postgres_user,
    password=settings.postgres_password.get_secret_value(),
    host=settings.postgres_host,
    port=settings.postgres_port,
    database=settings.postgres_db,
)

engine = create_engine(database_url)

def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session