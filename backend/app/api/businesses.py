from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.schemas.business import BusinessCreate, BusinessResponse
from app.services.business import create_business

router = APIRouter(
    prefix="/api/v1/businesses",
    tags=["Businesses"],
)


@router.post(
    "/",
    response_model=BusinessResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_business_endpoint(
    business_data: BusinessCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_business(
        db=db,
        business_data=business_data,
        owner=current_user,
    )