"""Initialization of APISpec with info from BaseResource subclasses and tags."""

import toml

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from ..resources import BaseResource
from config import Config

# Load data from tool.poetry section of the pyproject.toml file
pyproject = toml.load("pyproject.toml")["tool"]["poetry"]


def build_specs():
    """Gather spec data from pyproject.toml and resource modules."""

    # Initialize APISpec info object with poetry fields
    spec = APISpec(
        title=pyproject["name"],
        version=pyproject["version"],
        openapi_version=Config.OPENAPI_VERSION,
        info=dict(
            description=pyproject["description"],
            license={"name": pyproject["license"]},
        ),
        plugins=[MarshmallowPlugin()],
    )

    # Append each resource to spec paths object, sorted by path
    for cls in sorted(
        BaseResource.__subclasses__(), key=lambda instance: instance.path
    ):
        spec.path(path=cls.path, operations=cls.operations if cls.operations else None)

    return spec


def add_specs():
    """Dump OpenAPI spec as yaml file for client consumption."""

    f = open("openapi_spec.yaml", "w")
    f.write(build_specs().to_yaml(yaml_dump_kwargs={"sort_keys": False}))
    f.close()
