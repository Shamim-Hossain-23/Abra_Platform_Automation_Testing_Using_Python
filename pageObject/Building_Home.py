import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from testCases.Abra_Base import BaseDriver
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select


class AddHome(BaseDriver):
    lnk_home_xpath = "//span[normalize-space()='Homes']"
    lnk_add_home_xpath = "//button[@class='awp-btn transparent-btn ml-2']"
    select_building_id = "building"
    dropdown_xpath = "//div[@class='p-dropdown-panel p-component']"
    input_home_number_id = "home-number"
    input_flore_number = "floor-input"
    btn_add_home_xpath = "//button[@type='submit']"
    btn_save_xpath = "//button[normalize-space()='Save']"
    # //ul[@role='listbox']/li[@aria-label='Testing add building(Anan)']

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_home_lnk(self):
        self.wait_for_presence_of_all_elements(By.XPATH, self.lnk_home_xpath)
        self.driver.find_element(By.XPATH, self.lnk_home_xpath).click()

    def click_add_home_lnk(self):
        self. wait_until_element_is_clickable(By.XPATH, self.lnk_add_home_xpath)
        self.driver.find_element(By.XPATH, self.lnk_add_home_xpath).click()

    def select_building_selector(self, expected_text):
        self. wait_until_element_is_clickable(By.ID, self.select_building_id)
        element = self.driver.find_element(By.ID, self.select_building_id)
        drop_down = Select(element)
        drop_down.select_by_visible_text(expected_text)

    def add_home_number(self, home_number):
        number = self.driver.find_element(By.XPATH, self.input_home_number_id)
        number.click()
        number.send_keys(home_number)

    def click_add_home_button(self):
        self.driver.find_element(By.ID, self.btn_add_home_xpath).click()

    def click_save_button(self):
        self.driver.find_element(By.ID, self.btn_save_xpath).click()



