from fastapi import FastAPI
from app.users.router import router as users_router

from app.tickets.router import router as tickets_router

app = FastAPI()

app.include_router(tickets_router)
app.include_router(users_router)

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}