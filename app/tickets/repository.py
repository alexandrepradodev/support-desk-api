from sqlalchemy import select
from sqlalchemy.orm import Session

from app.tickets.models import Ticket

def list_tickets(session: Session) -> list[Ticket]:
    query = select(Ticket).order_by(Ticket.id)
    return list(session.scalars(query))

def add_ticket(
        session: Session,
        title: str,
        description: str,
        requester_id: int,
) -> Ticket:
    ticket = Ticket(
        title=title,
        description=description,
        requester_id=requester_id
    )
    session.add(ticket)
    return ticket