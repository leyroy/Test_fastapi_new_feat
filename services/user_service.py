from schemas.user import UserCreate

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.exceptions import ConflictError
from core.security import hash_password
from models.user import User


async def get_by_email(session: AsyncSession, email: str) -> User | None:
    result = await session.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def create(session: AsyncSession, data: UserCreate) -> User:
    if await get_by_email(session, data.email):
        raise ConflictError("Email already registered")

    user = User(
        email=data.email,
        full_name=data.full_name,
        hashed_password=hash_password(data.password),
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user