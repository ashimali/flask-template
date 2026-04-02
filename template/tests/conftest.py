import pytest
from application.factory import create_app
from application.extensions import db as _db


@pytest.fixture(scope="session")
def app():
    app = create_app("application.config.TestConfig")
    yield app


@pytest.fixture(scope="session")
def db(app):
    with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()
