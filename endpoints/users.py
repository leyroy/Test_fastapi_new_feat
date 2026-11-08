from fastapi import APIRouter, status

from deps import CurrentUser, SessionDep
from schemas.user import UserCreate, UserPublic
from services import user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate, session: SessionDep):
    return await user_service.create(session, payload)


@router.get("/me", response_model=UserPublic)
async def read_me(current_user: CurrentUser):
    return current_user


