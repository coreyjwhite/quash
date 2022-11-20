"""REST endpoint for root path to return path directory."""

from marshmallow import Schema, fields

from .base import BaseResource
from ..utils import get_all_subclasses


class RootSchema(Schema):
    directory = fields.List(
        fields.String(),
        metadata={"example": ["/", "/info", "/openapi", "/ping", "/weather/forecast"]},
    )


class RootResource(BaseResource):

    path = "/"
    schema = RootSchema
    operations = {
        "get": {
            "tags": ["info"],
            "summary": "Get a dictionary of API paths",
            "responses": {
                200: {
                    "description": "OK",
                    "content": {"application/json": {"schema": schema}},
                }
            },
        }
    }

    def get(self):
        """Return a list of endpoints."""

        return {
            "directory": [
                resource.path
                for resource in sorted(
                    get_all_subclasses(BaseResource),
                    key=lambda instance: instance.path,
                )
            ]
        }
