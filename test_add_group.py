
from model.mgroup import Group


def test_add_group(app):
    app.group.create(Group(name="test1", header="test", footer="test, test! test?"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))




