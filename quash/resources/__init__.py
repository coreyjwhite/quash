"""Single function to gather and expose REST resources and endpoints from submodules."""

from .base import BaseResource
from . import info, openapi, ping, root
from ..utils import get_all_subclasses


def add_resources(api):
    """Add REST endpoints to the api instance from BaseResource subclasses."""

    for resource in get_all_subclasses(BaseResource):
        api.add_resource(resource, resource.get_path())
