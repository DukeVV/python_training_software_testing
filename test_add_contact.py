from model.mcontact import Contact


def test_create_new(app):
    app.contact.create_new(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov"))





