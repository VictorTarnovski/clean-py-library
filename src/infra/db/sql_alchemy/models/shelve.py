from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import uuid

class ShelveTable(Base):
    __tablename__ = "shelves"

    id: Mapped[uuid.uuid4().__class__] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
