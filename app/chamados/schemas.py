from pydantic import BaseModel, Field


class ChamadoCreate(BaseModel):
    titulo: str = Field(min_length=3, max_length=100)
    descricao: str

class ChamadoRead(ChamadoCreate):
    id: int
    status: str