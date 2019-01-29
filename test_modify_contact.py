
from model.mcontact import Contact


def test_modify_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="Sergei"))


def test_modify_middlename(app):
    app.contact.modify_first_contact(Contact(middlename="Sergeevich"))


def test_modify_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="Ivanov"))

