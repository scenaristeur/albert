from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, EmailStr, constr

from pyalbert.config import PASSWORD_PATTERN

if TYPE_CHECKING:
    from .stream import Stream

# ********
# * Misc *
# ********


class ContactForm(BaseModel):
    subject: str
    text: str
    institution: str | None = None


# ********
# * Auth *
# ********


class ConfirmUser(BaseModel):
    email: EmailStr
    is_confirmed: bool


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: constr(pattern=PASSWORD_PATTERN)

    model_config = ConfigDict(extra="forbid")


class User(UserBase):
    id: int
    is_confirmed: bool | None = None
    is_admin: bool

    model_config = ConfigDict(from_attributes=True)


class UserWithRelationships(User):
    streams: list["Stream"] | None