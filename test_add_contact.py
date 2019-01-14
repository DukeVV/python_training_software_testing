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
        self.login(wd, username="admin", password="secret")
        self.create_new_contact(wd, firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Vania", companyname="Macriac", addresscompany="Pariz", phone_home="009988776655",
                                phone_mobile="0998766544", phone_work="0998765544", email="mail@mail.ru", email2="mail2@mail.ru", homepage="www.macriac.com", day="10",
                                month="June", year="1978")
        self.logout(wd)

    def create_new_contact(self, wd, firstname, middlename, lastname, nickname, companyname, addresscompany, phone_home,
                           phone_mobile, phone_work, email, email2, homepage, day, month, year):
        wd.find_element_by_link_text("add new").click()
        # fill name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        # fill company inf
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(companyname)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(addresscompany)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(phone_home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(phone_mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(phone_work)
        # mails
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)
        # date of birth
        # Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("bday")).select_by_visible_text(day)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(month)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[40]").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(year)
        # input data base
        wd.find_element_by_xpath("//input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
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
