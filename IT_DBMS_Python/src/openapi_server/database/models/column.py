from sqlalchemy import Integer, Column, ForeignKey, String, Enum
from sqlalchemy.orm import relationship

from openapi_server.database.sql_alchemy import BaseORMModel
from openapi_server.models.column_type import ColumnType


class TableColumn(BaseORMModel):
    __tablename__ = "table_columns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(Enum(ColumnType))
    table_id = Column(Integer, ForeignKey("tables.id"))

    table = relationship("Table", back_populates="columns")
