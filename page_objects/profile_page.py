import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:

    # XPaths and IDs for various elements on the profile page
    icon_edit_xpath = "//span[text()='Resume headline']/following-sibling::span"
    text_headline_id = "resumeHeadlineTxt"
    button_save_headline_xpath = "//button[text()='Save']"
    input_resume_id = "attachCV"
    text_resume_name_xpath = '//*[@id="lazyAttachCV"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div'

    def __init__(self, driver):
        self.driver = driver

    def click_edit_headline(self):
        """Click the 'Edit' button for the headline."""
        self.driver.find_element(By.XPATH, self.icon_edit_xpath).click()

    def set_headline(self, headline):
        """Set the headline text."""
        headline_element = self.driver.find_element(By.ID, self.text_headline_id)
        headline_element.clear()
        headline_element.send_keys(headline)

    def click_save_headline(self):
        """Click the 'Save' button and return the confirmation message."""
        self.driver.find_element(By.XPATH, self.button_save_headline_xpath).click()
        message = self.driver.execute_script(
            "return document.evaluate(\"//p[@class='msg']\", document, null, XPathResult.STRING_TYPE, null).stringValue;")
        return message

    def get_headline(self):
        """Get the current headline text."""
        return self.driver.find_element(By.ID, self.text_headline_id).text

    def scroll_till_headline(self):
        """Scroll the page to bring the headline into view."""
        self.driver.execute_script("window.scrollBy(0, 700);")

    def click_update_resume(self, resume_path):
        """Upload or update the resume."""
        if os.path.exists(resume_path):
            self.driver.find_element(By.ID,self.input_resume_id).send_keys(resume_path)
        else:
            print("The resume file does not exist.")

    def get_resume_name(self):
        time.sleep(1)
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.text_resume_name_xpath))
        )
        return element.text
