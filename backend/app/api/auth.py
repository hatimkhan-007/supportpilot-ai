from fastapi import APIRouter, Depends

from app.api.deps import get_current_user

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
)


@router.get("/me")
def get_me(current_user: dict = Depends(get_current_user)):
    return {
        "uid": current_user.get("uid"),
        "email": current_user.get("email"),
        "email_verified": current_user.get("email_verified"),
    }