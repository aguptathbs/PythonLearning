import unittest
from selenium.webdriver import Chrome
from login_page import LoginPage
#from learning.selenium.POM.gmail import create_driver

class Testlogin512345(unittest.TestCase):

    def setUp(self):
        #Browser Initialization
        self.driver = Chrome('chromedriver.exe')
        #self.driver = create_driver.get_browser_instance()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.gmail.com")

        #page object class intialization
        self.login = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_usename_textbox_123431(self):
        #wait for page to load
        self.login.wait_for_login_page_to_load()

        #verify username
        un_type = self.login.get_usename_textbox().get_attribute('type')

        assert un_type == "email"

        #click next button
        actual_is_enabled = self.login.next_button().is_enabled()
        expected_is_enabled = True

        assert expected_is_enabled == actual_is_enabled

#python -m pytest C:\AllPythonProjects\PythonLearning\learning\selenium\POM\gmail\gmail_login.py -s -v
