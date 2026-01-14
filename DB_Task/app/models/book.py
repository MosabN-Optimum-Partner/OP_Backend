# from library import Library
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.DatabaseMigration import db
if TYPE_CHECKING:
    from .library import Library
class Book(db.Model):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column(nullable=False)
    library_id: Mapped[int] = mapped_column(ForeignKey("library.id"))

    library: Mapped["Library"]= relationship(back_populates="books")
