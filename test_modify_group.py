
from model.mgroup import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New Name"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))

