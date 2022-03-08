import time

from selenium.webdriver.common.by import By

from testCases.Abra_Base import BaseDriver


class AddBuilding(BaseDriver):
    # Part - 1
    lnk_buildings_xpath = "//span[normalize-space()='Buildings']"
    btn_add_building_xpath = "//button[@type='button']"
    txt_building_title_id = "buildingTitle"
    txt_address_id = "address"
    txt_zip_code_id = "zipCode"
    txt_city_id = "city"
    txt_country_id = "country"
    txt_farm_number_id = "gårdsnummer"  # gårdsnummer
    txt_property_unity_number_id = "propertyUnityNumber"
    btn_next_xpath = "//button[normalize-space()='Next']"
    # Part - 2
    upload_header_image_id = "awpImgUploader"
    select_select_building_type_id = "buildingType"
    select_select_construction_type_id = "constructionType"
    txt_building_year_id = "buildingYear"
    txt_no_of_floors_id = "floors"
    txt_no_of_parking_lots_id = "parkingLots"
    btn_back_xpath = "//button[normalize-space()='Back']"
    btn_save_building_xpath = "//button[normalize-space()='Save Building']"

    # Building type custom xpath
    building_type_xpath = "//div[@class='p-dropdown-items-wrapper']/ul/li[text()='"

    # Construction type custom xpath
    construction_type_xpath = "//div[@class='p-dropdown-items-wrapper']/ul/li[text()='"

    # Custom Building title xpath verify
    buildings_title_verify = "//h2[normalize-space()='"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_buildings_manu(self):
        self.wait_for_presence_of_all_elements(By.XPATH, self.lnk_buildings_xpath)
        self.driver.find_element_by_xpath(self.lnk_buildings_xpath).click()

    def click_on_add_building_button(self):
        self.driver.find_element_by_xpath(self.btn_add_building_xpath).click()

    def set_building_title(self, title):
        building_title_driver = self.driver.find_element_by_id(self.txt_building_title_id)
        # building_title_driver = self.wait_until_element_is_clickable(By.XPATH, self.txt_building_title_xpath)
        building_title_driver.click()
        building_title_driver.send_keys(title)

    def set_address(self, address):
        address_driver = self.driver.find_element_by_id(self.txt_address_id)
        address_driver.click()
        address_driver.send_keys(address)

    def set_zip_code(self, zip_code):
        zip_code_driver = self.driver.find_element_by_id(self.txt_zip_code_id)
        zip_code_driver.click()
        zip_code_driver.send_keys(zip_code)

    def set_city(self, city):
        city_driver = self.driver.find_element_by_id(self.txt_city_id)
        city_driver .click()
        city_driver .send_keys(city)

    def set_country(self, country):

        country_driver = self.driver.find_element_by_id(self.txt_country_id)
        country_driver.click()
        country_driver.send_keys(country)

    def set_farm_number(self, farm_number):
        farm_number_driver = self.driver.find_element_by_id(self.txt_farm_number_id)
        farm_number_driver.click()
        farm_number_driver.send_keys(farm_number)

    def set_property_unity_number(self, property_unity_number):
        unity_umber_driver = self.driver.find_element_by_id(self.txt_property_unity_number_id)
        unity_umber_driver.click()
        unity_umber_driver.send_keys(property_unity_number)

    def click_on_next_button(self):
        self.driver.find_element_by_xpath(self.btn_next_xpath).click()

    def select_building_type(self, building_type):
        building_type_driver = self.driver.find_element_by_id(self.select_select_building_type_id)
        building_type_driver.click()
        time.sleep(2)
        b_xpath = self.building_type_xpath + building_type + "']"
        item = self.driver.find_element_by_xpath(b_xpath)
        item.click()

    def select_construction(self, construction_type_name):
        building_type_driver = self.driver.find_element_by_id(self.select_select_construction_type_id)
        building_type_driver.click()
        time.sleep(2)
        b_xpath = self.construction_type_xpath + construction_type_name + "']"
        item = self.driver.find_element_by_xpath(b_xpath)
        item.click()

    def set_building_year(self, year):
        year_driver = self.driver.find_element_by_id(self.txt_building_year_id)
        year_driver.click()
        year_driver.send_keys(year)

    def set_no_of_floors(self, floors):
        floors_driver = self.driver.find_element_by_id(self.txt_no_of_floors_id)
        floors_driver.click()
        floors_driver.send_keys(floors)

    def set_no_of_parking_lots(self, parking_lots):
        parking_lots_driver = self.driver.find_element_by_id(self.txt_no_of_parking_lots_id)
        parking_lots_driver.click()
        parking_lots_driver.send_keys(parking_lots)

    def click_on_back_button(self):
        self.driver.find_element_by_xpath(self.btn_back_xpath).click()

    def click_on_save_building_button(self):
        self.driver.find_element_by_xpath(self.btn_save_building_xpath).click()

    def upload_file(self, file_path):
        upload = self.driver.find_element_by_id(self.upload_header_image_id)
        upload.send_keys(file_path)

    def verify_add_building(self, title):
        new_xpath = self.buildings_title_verify + title + "']"
        return self.driver.find_element(By.XPATH, new_xpath).text

    def add_building_step_1(self, title, address, zip_code, city, country, farm_number, property_unity_number):
        time.sleep(3)
        self.set_building_title(title)
        self.set_address(address)
        self.set_zip_code(zip_code)
        self.set_city(city)
        self.set_country(country)
        self.set_farm_number(farm_number)
        self.set_property_unity_number(property_unity_number)

    def add_building_step_2(self, file_path, building_type_name, construction_type_name, building_year, floors, parking_lots):
        time.sleep(1)
        self.upload_file(file_path)
        time.sleep(1)
        self.select_building_type(building_type_name)
        time.sleep(1)
        self.select_construction(construction_type_name)
        time.sleep(1)
        self.set_building_year(building_year)
        time.sleep(1)
        self.set_no_of_floors(floors)
        time.sleep(1)
        self.set_no_of_parking_lots(parking_lots)



