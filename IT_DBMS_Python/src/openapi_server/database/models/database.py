from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship

from openapi_server.database.sql_alchemy import BaseORMModel


class Database(BaseORMModel):
    __tablename__ = "databases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    tables = relationship("Table", back_populates="database", cascade="all, delete")
