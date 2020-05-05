from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage():

    def __init__(self,driver):
        self.driver = driver

    def wait_for_login_page_to_load(self):
        wait = WebDriverWait(driver = self.driver, timeout=30)

        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_class_name("xkfVF")))

    def get_usename_textbox(self):
        try:
            return self.driver.find_element_by_xpath("//input[@type=\'email\']")
        except:
            return None

    def next_button(self):
        try:
            return self.driver.find_element_by_css_selector(".RveJvd.snByac")
        except:
            return None
