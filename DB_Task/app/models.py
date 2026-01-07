from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.DatabaseMigration import db

class Book(db.Model):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column(nullable=False)
    library_id: Mapped[int] = mapped_column(ForeignKey("library.id"))

    library: Mapped["Library"]= relationship(back_populates="books")

class Library(db.Model):
    __tablename__ = "library"
    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)

    books: Mapped[list["Book"]]= relationship(
        back_populates="library",cascade="all, delete-orphan")
