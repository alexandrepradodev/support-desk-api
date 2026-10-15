from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.tickets.repository import list_tickets
from app.tickets.schemas import TicketRead, TicketCreate
from app.tickets.service import RequesterNotFoundError, create_ticket

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.get("/", response_model=list[TicketRead])
async def read_tickets(
    session: Annotated[AsyncSession, Depends(get_async_session)],
) -> list[TicketRead]:
    tickets = await list_tickets(session)
    return [TicketRead.model_validate(ticket) for ticket in tickets]

@router.post("/", response_model=TicketRead, status_code=201)
async def register_ticket(
    data: TicketCreate,
    session: Annotated[AsyncSession, Depends(get_async_session)],
) -> TicketRead:
    try:
        ticket = await create_ticket(
            session,
            title=data.title,
            description=data.description,
            requester_id=data.requester_id
        )
    except RequesterNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Usuário solicitante não encontrado"
        ) from None
    return TicketRead.model_validate(ticket)