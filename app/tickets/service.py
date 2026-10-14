from sqlalchemy.orm import Session

from app.users.repository import get_user_by_id
from app.tickets.models import Ticket
from app.tickets.repository import add_ticket

class RequesterNotFoundError(Exception):
    pass

def create_ticket(
        session: Session,
        title: str,
        description: str,
        requester_id: int
) -> Ticket:
    if get_user_by_id(session, requester_id) is None:
        raise RequesterNotFoundError()

    ticket = add_ticket(
        session,
        title=title,
        description=description,
        requester_id=requester_id
    )
    session.commit()
    session.refresh(ticket)
    return ticket

