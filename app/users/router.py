from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_session
from app.users.schemas import UserCreate, UserRead
from app.users.service import EmailAlreadyRegisteredError, create_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead, status_code=201)
def register_user(
    data: UserCreate,
    session: Annotated[Session, Depends(get_session)],
) -> UserRead:
    try:
        user = create_user(
            session,
            email=data.email,
            password=data.password.get_secret_value(),
        )
    except EmailAlreadyRegisteredError:
        raise HTTPException(status_code=409, detail="Email já cadastrado") from None

    return UserRead.model_validate(user)