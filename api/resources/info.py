"""REST endpoint for returning API server config and version information."""

import json
import platform

from marshmallow import Schema, fields
import toml

from .base import BaseResource
from .. import db


class InnerSchema(Schema):
    """Schema of response to /info."""

    platform = fields.String(
        required=True,
        metadata={"example": "Linux-4.4.0-19041-Microsoft-x86_64-with-glibc2.29"},
    )
    machine_name = fields.String(required=True, metadata={"example": "dev-machine"})
    python_version = fields.String(required=True, metadata={"example": "3.8.10"})
    api_version = fields.String(required=True, metadata={"example": "0.3.0"})
    database = fields.String(required=True, metadata={"example": "my_db"})
    db_version = fields.String(
        required=True, metadata={"example": "10.4.22-MariaDB-1:10.4.22+maria~focal-log"}
    )


class InfoSchema(Schema):
    info = fields.Nested(InnerSchema)


class InfoResource(BaseResource):

    path = "/info"
    schema = InfoSchema
    operations = {
        "get": {
            "summary": "Get server configuration and version information",
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
        """Return server info."""

        # Load poetry configuration data
        api_version = toml.load("pyproject.toml")["tool"]["poetry"]["version"]
        db_name = db.session.bind.url.database
        db_version = db.session.execute("SELECT VERSION()").first()[0]

        return {
            "info": {
                "platform": platform.platform(),
                "machine_name": platform.node(),
                "python_version": platform.python_version(),
                "api_version": api_version,
                "database": db_name,
                "db_version": db_version,
            },
        }
