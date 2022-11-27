"""Injection of generated marshmallow schemas into SQLAlchemy model classes.

Adapted from https://marshmallow-sqlalchemy.readthedocs.io/en/latest/recipes.html#automatically-generating-schemas-for-sqlalchemy-models
"""

from marshmallow_sqlalchemy import ModelConversionError, SQLAlchemyAutoSchema


def setup_schema(db):
    """Iterate over mapper classes and set marshmallow schema attributes."""

    for class_ in db.Model.registry._class_registry.values():
        if hasattr(class_, "__tablename__"):
            if class_.__name__.endswith("Schema"):
                raise ModelConversionError(
                    "For safety, setup_schema can not be used when a"
                    "Model class ends with 'Schema'"
                )

            class Meta(object):
                model = class_
                sqla_session = db.session

            schema_class_name = "%sSchema" % class_.__name__

            schema_class = type(
                schema_class_name, (SQLAlchemyAutoSchema,), {"Meta": Meta}
            )

            setattr(class_, "__marshmallow__", schema_class)
