"""REST endpoint for the OpenAPI specification YAML file."""

from marshmallow import Schema, fields
import yaml

from .base import BaseResource
from .. import db


class OpenApiSchema(Schema):
    info = fields.Dict(required=True)
    paths = fields.Dict(required=True)
    openapi = fields.String(required=True)
    components = fields.Dict(required=True)


class OpenApiResource(BaseResource):

    path = "/openapi"
    schema = OpenApiSchema
    operations = {
        "get": {
            "summary": "Get the OpenAPI specification",
            "tags": ["info"],
            "responses": {
                200: {
                    "description": "OK",
                    "content": {"application/json": {"schema": schema}},
                }
            },
        }
    }

    def get(self):
        """Return OpenAPI spec YAML from root dir."""

        with open("openapi_spec.yaml", "r") as stream:
            data_loaded = yaml.safe_load(stream)

        return data_loaded
