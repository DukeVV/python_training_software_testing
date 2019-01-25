from model.mcontact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create_new(self, firstname, middlename, lastname):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        # fill name
        self.fill_name(Contact(firstname=firstname, middlename=middlename, lastname=lastname))
        # input data base
        wd.find_element_by_xpath("//input[21]").click()


    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletein
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(60)

    def edit_first_contact(self, firstname, middlename, lastname):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill name
        self.fill_name(Contact(firstname=firstname, middlename=middlename, lastname=lastname))
        # input data base
        wd.find_element_by_name("update").click()

    def fill_name(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)