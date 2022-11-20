"""Extension of Flask-RESTful Resource class."""

from flask_restful import Resource


class BaseResource(Resource):

    # Replace any {} in OpenAPI documentation wtih <> for Flask
    @classmethod
    def get_path(cls):
        """Return a path with angle bracketed parameter for Flask routing."""

        trans = cls.path.maketrans("{}", "<>")
        return cls.path.translate(trans)
