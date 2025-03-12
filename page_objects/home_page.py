from selenium.webdriver.common.by import By

class HomePage:
    button_view_profile_xpath = '//a[@href="/mnjuser/profile"]'

    def __init__(self,driver):
        self.driver = driver

    def click_view_profile(self):
        self.driver.find_element(By.XPATH, self.button_view_profile_xpath).click()



