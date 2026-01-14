from sqlalchemy import ForeignKey
# from library import Library
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.DatabaseMigration import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .library import Library

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    library_id: Mapped[int] = mapped_column(ForeignKey("library.id"), nullable=True)


    library: Mapped["Library"] = relationship("Library", back_populates="user", uselist=False)

