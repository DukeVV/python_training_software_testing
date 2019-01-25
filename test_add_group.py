

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(name="test1", header="test", footer="test, test! test?")
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(name="", header="", footer="")
    app.session.logout()




