from sqlalchemy import select
from sqlalchemy.orm import Session

from app.tickets.models import Ticket

def list_tickets(session: Session) -> list[Ticket]:
    query = select(Ticket).order_by(Ticket.id)
    return list(session.scalars(query))
