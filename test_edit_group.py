

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(name="test2", header="test2, test2, test2", footer="test2")
    app.session.logout()
