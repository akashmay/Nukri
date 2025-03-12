import time
import pytest

from page_objects.home_page import HomePage
from page_objects.profile_page import ProfilePage
from page_objects.login_page import LoginPage
from utilities import read_properties


class TestUpdateHeadline:

    def test_update_headline(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(read_properties.read_baseurl())

        # Login Process
        self.login_page = LoginPage(self.driver)
        # self.login_page.click_login_page_button()
        self.login_page.set_email(read_properties.read_login_username())
        self.login_page.set_password(read_properties.read_password())
        self.login_page.click_login_button()

        # Navigate to Profile
        self.home_page = HomePage(self.driver)
        self.home_page.click_view_profile()
        self.profile_page = ProfilePage(self.driver)

        # Edit Headline
        self.profile_page.click_edit_headline()
        headline = self.profile_page.get_headline()
        headline1 = read_properties.read_headline(1)
        headline2 = read_properties.read_headline(2)

        # Verify and update headline
        if "Proficient in Python" in headline:
            self.profile_page.set_headline(headline2)
        elif "Expert in Python" in headline:
            self.profile_page.set_headline(headline1)
        else:
            pytest.fail(f"Unexpected headline value: {headline}")

        self.profile_page.click_save_headline()

        # Assertion to verify if the headline was updated
        updated_headline = self.profile_page.get_headline()
        assert updated_headline == headline2 or updated_headline == headline1, \
            f"Headline not updated correctly. Expected one of {headline1} or {headline2}, but got {updated_headline}"
