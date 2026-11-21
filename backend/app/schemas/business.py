
from pydantic import BaseModel, Field, ConfigDict


class BusinessCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=255,
        description="Name of the business",
    )

    description: str | None = Field(
        default=None,
        max_length=2000,
    )


class BusinessResponse(BaseModel):
    id: int
    name: str
    slug: str
    description: str | None
    owner_id: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
