from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from openapi_server.database.sql_alchemy import BaseORMModel


class Table(BaseORMModel):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    database_id = Column(Integer, ForeignKey("databases.id"))

    database = relationship("Database", back_populates="tables")
    columns = relationship("TableColumn", back_populates="table", cascade="all, delete")