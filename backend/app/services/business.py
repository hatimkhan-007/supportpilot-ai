import re
import uuid

from sqlalchemy.orm import Session

from app.models.business import Business
from app.models.user import User


def generate_slug(name: str) -> str:
    base_slug = re.sub(
        r"[^a-z0-9]+",
        "-",
        name.lower()
    ).strip("-")

    return f"{base_slug}-{uuid.uuid4().hex[:6]}"


def create_business(
    db: Session,
    business_data,
    owner: User,
) -> Business:

    business = Business(
        name=business_data.name,
        slug=generate_slug(business_data.name),
        description=business_data.description,
        owner_id=owner.id,
    )

    db.add(business)
    db.commit()
    db.refresh(business)

    return business

def get_user_businesses(
    db: Session,
    owner: User,
) -> list[Business]:

    return (
        db.query(Business)
        .filter(Business.owner_id == owner.id)
        .order_by(Business.created_at.desc())
        .all()
    )

def get_business_by_id(
    db: Session,
    business_id: int,
    owner: User,
) -> Business | None:

    return (
        db.query(Business)
        .filter(
            Business.id == business_id,
            Business.owner_id == owner.id,
        )
        .first()
    )

def update_business(
    db: Session,
    business_id: int,
    business_data,
    owner: User,
) -> Business | None:

    business = get_business_by_id(
        db=db,
        business_id=business_id,
        owner=owner,
    )

    if not business:
        return None

    business.name = business_data.name
    business.description = business_data.description

    db.commit()
    db.refresh(business)

    return business

def delete_business(
    db: Session,
    business_id: int,
    owner: User,
) -> bool:

    business = get_business_by_id(
        db=db,
        business_id=business_id,
        owner=owner,
    )

    if not business:
        return False

    db.delete(business)
    db.commit()

    return True