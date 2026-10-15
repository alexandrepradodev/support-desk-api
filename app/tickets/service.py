
from sqlalchemy.ext.asyncio import AsyncSession

from app.users.repository import get_user_by_id
from app.tickets.models import Ticket
from app.tickets.repository import add_ticket, fetch_tickets



class RequesterNotFoundError(Exception):
    pass

async def create_ticket(
        session: AsyncSession,
        title: str,
        description: str,
        requester_id: int
) -> Ticket:
    if (await get_user_by_id(session, requester_id)) is None:
        raise RequesterNotFoundError()

    ticket = add_ticket(
        session,
        title=title,
        description=description,
        requester_id=requester_id
    )
    await session.commit()
    await session.refresh(ticket)
    return ticket

async def list_tickets(
    session: AsyncSession
) -> list[Ticket]:
    return await fetch_tickets(session)

