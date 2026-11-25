from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.schemas.business import BusinessCreate, BusinessResponse
from app.services.business import create_business
from app.services.business import get_user_businesses
from app.services.business import get_business_by_id
from app.services.business import update_business
from app.services.business import delete_business

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

@router.get(
    "/",
    response_model=list[BusinessResponse],
)
def list_businesses_endpoint(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_user_businesses(
        db=db,
        owner=current_user,
    )

@router.get(
    "/{business_id}",
    response_model=BusinessResponse,
)
def retrieve_business_endpoint(
    business_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    business = get_business_by_id(
        db=db,
        business_id=business_id,
        owner=current_user,
    )

    if not business:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Business not found",
        )

    return business


@router.put(
    "/{business_id}",
    response_model=BusinessResponse,
)
def update_business_endpoint(
    business_id: int,
    business_data: BusinessCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    business = update_business(
        db=db,
        business_id=business_id,
        business_data=business_data,
        owner=current_user,
    )

    if not business:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Business not found",
        )

    return business


@router.delete(
    "/{business_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_business_endpoint(
    business_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    deleted = delete_business(
        db=db,
        business_id=business_id,
        owner=current_user,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Business not found",
        )