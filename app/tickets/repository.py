from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.tickets.models import Ticket



async def list_tickets(session: AsyncSession) -> list[Ticket]:
    query = select(Ticket).order_by(Ticket.id)
    result = await session.scalars(query)
    return list(result)

def add_ticket(
        session: AsyncSession,
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