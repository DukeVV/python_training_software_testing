
import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.desrtoy)
    return fixture


def test_untitled_test_case(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov"))
    app.session.logout()






