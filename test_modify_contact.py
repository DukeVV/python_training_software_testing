
from model.mcontact import Contact


def test_modify_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Sergei"))
    app.session.logout()


def test_modify_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(middlename="Sergeevich"))
    app.session.logout()


def test_modify_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="Ivanov"))
    app.session.logout()

