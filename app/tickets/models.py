from sqlalchemy import ForeignKey, String, Text, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.tickets.status import TicketStatus

from app.db.base import Base

class Ticket(Base):
    __tablename__ = "tickets"

    __table_args__ = (
        CheckConstraint(
            "status IN ('open', 'in_progress', 'closed')",
            name="ck_tickets_status",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, server_default=TicketStatus.OPEN.value
        )
    requester_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )