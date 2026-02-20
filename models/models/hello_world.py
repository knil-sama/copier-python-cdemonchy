from uuid import UUID, uuid5

from pydantic import (
    BaseModel,
    Field
)

class HelloWorld(BaseModel):
    value: str