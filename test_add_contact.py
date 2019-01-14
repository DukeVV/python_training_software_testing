# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_new_contact(wd)
        self.logout(wd)

    def create_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()
        # fill name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Ivan")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Ivanovich")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Ivanov")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("Vania")
        # fill company inf
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Macriac")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Pariz")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("009988776655")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("0998766544")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("0998765544")
        # mails
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("mail@mail.ru")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("mail2@mail.ru")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("www.macriac.com")
        # date of birth
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("10")
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("June")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[40]").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1978")
        # input data base
        wd.find_element_by_xpath("//input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
