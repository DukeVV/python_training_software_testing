
from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Sergei", middlename="Ivanovich", lastname="Sergeev"))
    app.session.logout()