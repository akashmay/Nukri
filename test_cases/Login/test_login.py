import time
from page_objects.login_page import LoginPage
from utilities import read_properties
import pytest



class TestLogin:

    def test_login(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(read_properties.read_baseurl())

        self.login_page = LoginPage(self.driver)
        self.login_page.click_login_page_button()
        self.login_page.set_email(read_properties.read_login_username())
        self.login_page.set_password(read_properties.read_password())
        self.login_page.click_login_button()

        time.sleep(2)
        return self.driver
