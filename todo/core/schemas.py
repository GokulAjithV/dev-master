from pydantic import BaseModel, ConfigDict

class TodoCreate(BaseModel):
    title: str
    note: str | None = None
    completed: bool = False

class TodoCreateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    note: str | None
    completed: bool