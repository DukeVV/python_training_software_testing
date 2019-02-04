from model.contact import Contact


def test_modify_firstname(app):
    app.contact.check_contact()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Sergei", middlename="Ivanovich", lastname="Sergeev")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



#def test_modify_middlename(app):
#    app.contact.check_contact()
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(firstname="Sergei", middlename="Ivanovich", lastname="Sergeev"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_lastname(app):
#    app.contact.check_contact()
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(firstname="Sergei", middlename="Ivanovich", lastname="Sergeev"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
