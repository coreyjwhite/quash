"""General utilites."""

from . import marshmallow, sqla


def get_all_subclasses(cls):
    """Recursively return all subclasses."""

    all_subclasses = []

    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses
