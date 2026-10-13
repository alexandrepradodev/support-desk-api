from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_session
from app.tickets.repository import list_tickets
from app.tickets.schemas import TicketRead

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.get("/", response_model=list[TicketRead])
def read_tickets(
    session: Annotated[Session, Depends(get_session)],
) -> list[TicketRead]:
    tickets = list_tickets(session)
    return [TicketRead.model_validate(ticket) for ticket in tickets]