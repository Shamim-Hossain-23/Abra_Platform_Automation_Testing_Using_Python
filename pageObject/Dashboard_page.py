import time
from selenium.webdriver.common.by import By
from testCases.Abra_Base import BaseDriver


class Dashboard(BaseDriver):
    p_water_xpath = "//p[normalize-space()='Water']"
    p_hub_xpath = "//p[contains(text(),'Hub')]"
    p_fire_xpath = "//p[contains(text(),'Fire')]"
    p_alarm_xpath = "//p[contains(text(),'Alarm')]"
    img_btn_register_building_xpath = "//div[@class='card mb-0']//div[1]//div[3]"
    img_btn_invite_home_owner_xpath = "//div[@id='action-row']//div[2]//div[3]"
    img_btn_register_home_index_xpath = "(//img[@alt='mylogo'])[6]"
    img_btn_connect_hubs_xpath = "//div[4]//div[3]//img[1]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_water_name(self):
        time.sleep(3)
        return self.driver.find_element_by_xpath(self.p_water_xpath).text

    def get_hub_name(self):
        return self.driver.find_element(By.XPATH, self.p_hub_xpath).text

    def get_fire_name(self):
        return self.driver.find_element(By.XPATH, self.p_fire_xpath).text

    def get_alarm_name(self):
        return self.driver.find_element(By.XPATH, self.p_alarm_xpath).text

    def get_all_links(self):
        links = self.driver.find_elements(By.TAG_NAME, "a")
        print(len(links))
        for link in links:
            print(link.text)

    def click_on_register_building_img_btn(self):
        self.driver.find_element(By.XPATH, self.img_btn_register_building_xpath).click()

    def click_on_invite_home_owner_img_btn(self):
        self.driver.find_element(By.XPATH, self.img_btn_invite_home_owner_xpath).click()

    def click_on_register_home_img_btn(self):
        self.driver.find_element(By.XPATH, self.img_btn_register_home_index_xpath).click()

    def click_on_connect_devices_img_btn(self):
        self.driver.find_element(By.XPATH, self.img_btn_connect_hubs_xpath).click()