"""Standard and test configuration classes."""

import importlib.metadata
import toml

pyproject = toml.load("/home/corey/api/pyproject.toml")["tool"]["poetry"]


class Config:

    # Flask options
    DEBUG = True

    # APScheduler options
    SCHEDULER_API_ENABLED = True

    # OpenAPI
    OPENAPI_VERSION = "3.0.2"

    # MySQL options
    MYSQL_USER = "myquash"
    MYSQL_PW = "nCZ6XikP"
    MYSQL_SERVER = "localhost"
    MYSQL_DB = "quash"

    # SQLAlchemy options
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable deprecated feature
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PW}@localhost/{MYSQL_DB}"

    ## Interface options

    DEFAULT_HTTP_USER_AGENT = f"python-requests/{importlib.metadata.version('requests')} {pyproject['name']}/{pyproject['version']}"

    # NWS API options
    NWS_DEFAULT_STATION = "KTYS"
    NWS_DEFAULT_GRID_X = "71"
    NWS_DEFAULT_GRID_Y = "53"

    # Toggl API options
    TOGGL_API_TOKEN = "6fb9dec465c17402f295ab55033be881"

    # YNAB API options
    YNAB_BASE_URL = "https://api.youneedabudget.com/v1"
    YNAB_ACCESS_TOKEN = "ftg8H_blqeFZOs6CoZKrFAUqDI9-sIif3qK8baS5cwE"
    YNAB_BUDGET_ID = "19e708d9-1191-476b-b2f1-9993e465cf04"


class TestConfig:

    ENV = "development"
    DEBUG = True

    MYSQL_USER = "myquash_test"
    MYSQL_PW = "quash_test_pw"
    MYSQL_SERVER = "localhost"
    MYSQL_DB = "quash_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable deprecated feature
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PW}@localhost/{MYSQL_DB}"
