from fastapi.testclient import TestClient

from main import app

from app.users import router as users_router
from app.users.service import EmailAlreadyRegisteredError

def test_register_user_rejects_invalid_email() -> None:
    response = TestClient(app).post(
        "/users",
        json={"email": "invalido", "password": "12345678"}
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "email"]


def test_register_user_returns_conflict_for_duplicate_email(monkeypatch) -> None:
    async def fake_create_user(*args, **kwargs):
        raise EmailAlreadyRegisteredError()

    monkeypatch.setattr(users_router, "create_user", fake_create_user)

    response = TestClient(app).post(
        "/users/",
        json={"email": "exemplo@email.com", "password": "12345678"}
    )

    assert response.status_code == 409
    assert response.json() == {"detail": "Email já cadastrado"}