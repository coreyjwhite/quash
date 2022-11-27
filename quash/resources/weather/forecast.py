"""REST endpoint for querying Meditech administration records."""

from flask import jsonify, request
from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import select
from webargs.flaskparser import use_args, use_kwargs

from ..base import BaseResource
from ... import db
from ...models.weather import NwsObservation


class ForecastRequestSchema(Schema):
    office = fields.Str(example="FFC")
    grid_x = fields.Int(example=42)
    grid_y = fields.Int(example=81)


class ForecastResource(BaseResource):

    path = "/weather/forecast"
    schema = NwsObservation.__marshmallow__()
    example = [
        {
            "date": "2020-21-11T06:27:00",
            "location": "3W",
            "mnemonic": "DIAZ5",
            "admin_dose": 2.5,
            "admin_dose_unit": "MG",
        }
    ]

    operations = {
        "post": {
            "tags": ["transactions"],
            "summary": "Weather forecast data",
            "parameters": [{"in": "query", "schema": ForecastRequestSchema}],
            "responses": {
                200: {
                    "description": "OK",
                    "content": {
                        "application/json": {
                            "schema": schema,
                            "example": example,
                        }
                    },
                },
                400: {"description": "No parameters received"},
            },
        }
    }

    @use_args(ForecastRequestSchema(), location="query")
    def get(self, args):
        # Return error if no query parameters
        if not request.args:
            return self.status_response("post", 400)

        # Parse parameters per operations documentation
        # pargs = self.parse_args("get", request.args)
        data = []

        for datum in data:
            forecast = NwsObservation(**datum)
            db.session.add(forecast)

        users = db.session.execute(select(NwsObservation))
        data = ForecastResource.schema.dump(users, many=True)
        return jsonify({"users": data})
