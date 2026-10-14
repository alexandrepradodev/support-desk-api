from sqlalchemy import select
from sqlalchemy.orm import Session

from app.users.models import User

def get_user_by_email(session: Session, email: str) -> User | None:
    query = select(User).where(User.email == email)
    return session.scalar(query)

def get_user_by_id(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)

def add_user(
        session: Session,
        email: str,
        password_hash: str,
        role: str
) -> User:
    user = User(email=email, password_hash=password_hash, role=role)
    session.add(user)
    return user