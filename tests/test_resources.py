"""Response testing module for API resources."""
# TODO conditional passing of parameters to test 400, 404, and 405 returns

from ..api import db, scheduler
from ..api.resources.base import BaseResource
from ..api.utils import get_all_subclasses


def test_all_resources(client):
    db.create_all()

    for job in scheduler.get_jobs():
        print(
            "name: %s, trigger: %s, next run: %s, handler: %s"
            % (job.name, job.trigger, job.next_run_time, job.func)
        )
        job.func()
    for subclass in get_all_subclasses(BaseResource):
        if subclass.schema:
            response = client.get(subclass.path)
            try:
                subclass.schema().loads(response.data)
                print("ok")
            except:
                print("error")
        assert response.status_code == 200
    db.drop_all()
