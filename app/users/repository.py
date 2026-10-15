from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.users.models import User

async def get_user_by_email(
        session: AsyncSession,
        email: str
) -> User | None:
    query = select(User).where(User.email == email)
    return await session.scalar(query)


async def get_user_by_id(
        session: AsyncSession,
        user_id: int,
) -> User | None:
    return await session.get(User, user_id)

async def fetch_users(
        session: AsyncSession
) -> list[User]:

    query = select(User).order_by(User.id)
    result = await session.scalars(query)
    return list(result)

def add_user(
        session: AsyncSession,
        email: str,
        password_hash: str,
        role: str
) -> User:
    user = User(email=email, password_hash=password_hash, role=role)
    session.add(user)
    return user