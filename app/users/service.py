from sqlalchemy.orm import Session

from app.security import hash_password
from app.users.models import User
from app.users.repository import add_user, get_user_by_email

class EmailAlreadyRegisteredError(Exception):
    pass

def create_user(session: Session, email: str, password: str) -> User:
    if get_user_by_email(session, email) is not None:
        raise EmailAlreadyRegisteredError()

    user = add_user(
        session,
        email=email,
        password_hash=hash_password(password),
        role="requester"
    )
    session.commit()
    session.refresh(user)
    return user