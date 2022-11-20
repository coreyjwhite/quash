"""Utility functions for SQLAlchemy."""

import sqlalchemy as sqla

from ..models.base import BaseModel
from ...config import Config


def create_table(table_names):
    """Create a single table from a model using the __tablename__(s)."""

    table_names = array_of(table_names)
    table_objects = [BaseModel.metadata.tables[table] for table in table_names]
    engine = sqla.create_engine(Config.SQLALCHEMY_DATABASE_URI)
    BaseModel.metadata.create_all(engine, tables=table_objects)
