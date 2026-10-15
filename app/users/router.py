from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.users.schemas import UserCreate, UserRead
from app.users.service import EmailAlreadyRegisteredError, create_user, list_users

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserRead])
async def read_users(
    session: Annotated[AsyncSession, Depends(get_async_session)],
) -> list[UserRead]:
    users = await list_users(session)
    return [UserRead.model_validate(user) for user in users]

@router.post("/", response_model=UserRead, status_code=201)
async def register_user(
    data: UserCreate,
    session: Annotated[AsyncSession, Depends(get_async_session)]
) -> UserRead:
    try:
        user = await create_user(
            session,
            email=data.email,
            password=data.password.get_secret_value()
        )
    except EmailAlreadyRegisteredError:
        raise HTTPException(status_code=409, detail="Email já cadastrado") from None

    return UserRead.model_validate(user)