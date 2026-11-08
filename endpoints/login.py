from fastapi import APIRouter

from schemas.user import UserPublic

router = APIRouter(prefix="/login", tags=["auth"])

@router.post("/", response_model=UserPublic)
def login():
  return {}