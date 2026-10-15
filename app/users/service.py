from sqlalchemy.ext.asyncio import AsyncSession
from starlette.concurrency import run_in_threadpool

from app.security import hash_password
from app.users.models import User
from app.users.repository import add_user, get_user_by_email

class EmailAlreadyRegisteredError(Exception):
    pass


async def create_user_async(
    session: AsyncSession,
    email: str,
    password: str
) -> User:
    if (await get_user_by_email(session, email)) is not None:
        raise EmailAlreadyRegisteredError()

    password_hash = await run_in_threadpool(hash_password, password)

    user = add_user(
        session,
        email=email,
        password_hash=password_hash,
        role="requester"
    )

    await session.commit()
    await session.refresh(user)
    return user