from pydantic import BaseModel, Field, ConfigDict

from app.tickets.status import TicketStatus


class TicketCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str

class TicketRead(TicketCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: TicketStatus
    requester_id: int