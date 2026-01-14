from typing import TYPE_CHECKING
# from .book import Book
# from .user import User
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.DatabaseMigration import db

if TYPE_CHECKING:
    # Use the single dot to look in the same folder
    from .book import Book
    from .user import User
class Library(db.Model):
    __tablename__ = "library"
    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)

    books: Mapped[list["Book"]]= relationship(
        back_populates="library",cascade="all, delete-orphan")
    
    user: Mapped["User"]= relationship("User", back_populates="library")