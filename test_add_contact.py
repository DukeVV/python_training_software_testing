
from model.contact import Contact


def test_create_new(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov"))
    app.session.logout()






