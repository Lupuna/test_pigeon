from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, Text, false, func
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database import Base, intpk


class Task(Base):
    __tablename__ = "task"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_completed: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default=false(), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
