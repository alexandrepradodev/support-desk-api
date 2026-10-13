from pydantic import BaseModel, ConfigDict, Field, EmailStr, SecretStr

class UserCreate(BaseModel):
    email: EmailStr
    password: SecretStr = Field(min_length=8)

class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    role: str