from selenium.webdriver.common.by import By

class LoginPage:

    # button_login_page_id = "login_Layer"
    input_email_xpath= "//input[@id='usernameField']"
    input_password_xpath = "//input[@id='passwordField']"
    button_login_xpath = "//button[normalize-space()='Login']"

    def __init__(self,driver):
        self.driver = driver


    def click_login_page_button(self):
        self.driver.find_element(By.ID,self.button_login_page_id).click()

    def set_email(self,email):
        input_box =self.driver.find_element(By.XPATH, self.input_email_xpath)
        input_box.send_keys(email)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def set_password(self,password):
        input_box =self.driver.find_element(By.XPATH, self.input_password_xpath)
        input_box.send_keys(password)