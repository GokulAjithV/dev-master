from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class TodoCreate(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    note: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)