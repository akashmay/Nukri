from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities import read_properties
from page_objects.profile_page import ProfilePage
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage

class TestUpdateResume:

    def test_update_resume(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(read_properties.read_baseurl())

        # Login Process
        self.login_page = LoginPage(self.driver)
        self.login_page.click_login_page_button()
        self.login_page.set_email(read_properties.read_login_username())
        self.login_page.set_password(read_properties.read_password())
        self.login_page.click_login_button()

        # Navigate to Profile
        self.home_page = HomePage(self.driver)
        self.home_page.click_view_profile()
        self.profile_page = ProfilePage(self.driver)

        # Update Resume

        resume_path1 = read_properties.read_resume_path(1).replace("\\","\\\\")
        resume_path2 = read_properties.read_resume_path(2).replace("\\","\\\\")

        resume_name = self.profile_page.get_resume_name()
        if resume_name in resume_path1:
            self.profile_page.click_update_resume(resume_path2)
            assert self.profile_page.get_resume_name() in resume_path2 , "resume not uploaded successfully"
        elif resume_name in resume_path2:
            self.profile_page.click_update_resume(resume_path1)
            assert self.profile_page.get_resume_name() in resume_path1 , "resume not uploaded successfully"

