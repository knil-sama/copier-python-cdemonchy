from uuid import UUID, uuid5

from pydantic import (
    BaseModel,
    Field
)

class HelloWorld(BaseModel):
    id: UUID =  Field(default_factory=lambda: uuid5())  # noqa: A003
    value: str