

def test_create_new(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov")
    app.session.logout()






