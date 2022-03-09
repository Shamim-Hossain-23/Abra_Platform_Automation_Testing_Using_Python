import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from pageObject.Login_page import LoginPage
# from utilities.ReadProperties import ReadConfig
from utilities.customLogger import LogGen


class BaseDriver:
    # baseURL = ReadConfig.getApplicationUrl()
    # username = ReadConfig.getUsername()
    # password = ReadConfig.getPassword()
    log = LogGen.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        # Get scroll height.
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:

            # Scroll down to the bottom.
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load the page.
            time.sleep(2)

            # Calculate new scroll height and compare with last scroll height.
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height
        time.sleep(4)

    # def login_test(self):
    #     lp = LoginPage(self.driver)
    #     lp.setUserName(self.username)
    #     lp.setPassword(self.password)
    #     lp.clickLogin()

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.presence_of_element_located((locator_type, locator)))

        return element

    def wait_until_element_is_clickable(self, locator_type, locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            # wait 10 seconds before looking for element
            element = wait.until(
                EC.element_to_be_clickable((locator_type, locator)))
        finally:
            self.driver.quit()
        return element
