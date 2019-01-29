
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_name(contact)
        # input data base
        wd.find_element_by_xpath("//input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def update_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def click_edit_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def fill_name(self, contact):
        wd = self.app.wd
        # fill name
        self.change_contact("firstname", contact.firstname)
        self.change_contact("middlename", contact.middlename)
        self.change_contact("lastname", contact.lastname)

    def change_contact(self, filde_contact, contact_text):
        wd = self.app.wd
        if contact_text is not None:
            wd.find_element_by_name(filde_contact).click()
            wd.find_element_by_name(filde_contact).clear()
            wd.find_element_by_name(filde_contact).send_keys(contact_text)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.click_edit_first_contact()
        self.fill_name(new_contact_data)
        self.update_contact()
