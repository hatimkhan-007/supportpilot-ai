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