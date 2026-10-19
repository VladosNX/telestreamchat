from sqlalchemy import String, Text, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from db import Base

class Message(Base):
    """A message from a Telegram group that should appear in the chat"""
    __tablename__ = 'messages'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    author_tgid: Mapped[int] = mapped_column(BigInteger)
    author_username: Mapped[str] = mapped_column(String(40))
    content: Mapped[str] = mapped_column(Text)

