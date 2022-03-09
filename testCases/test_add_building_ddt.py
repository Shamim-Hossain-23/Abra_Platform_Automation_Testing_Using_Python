import time
from pageObject.Login_page import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObject.Add_Building_pop_up import AddBuilding
from utilities import XLUtils


class TestAddBuilding:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGen.custom_logger()
    path = ".//TestData/AddBuildingdata.xlsx"

    def test_add_building_by_xlsx(self, setup):
        self.log.info("************* Test Add Building **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.log.info("************* Starting Login *************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.log.info("************* Login successful **********")

        self.add_building = AddBuilding(self.driver)
        time.sleep(10)
        self.add_building.click_on_buildings_manu()
        time.sleep(8)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')

        for r in range(2, self.rows + 1):
            self.add_building.click_on_add_building_button()
            time.sleep(3)
            self.log.info("************ Start The Add Building Step-1 ********** ")
            self.building_title = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.address = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.zip_code = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.city = XLUtils.readData(self.path, 'Sheet1', r, 4)
            self.country = XLUtils.readData(self.path, 'Sheet1', r, 5)
            self.farm_number = XLUtils.readData(self.path, 'Sheet1', r, 6)
            self.property_unity_number = XLUtils.readData(self.path, 'Sheet1', r, 7)
            self.add_building.add_building_step_1(self.building_title, self.address, self.zip_code, self.city,
                                                  self.country, self.farm_number, self.property_unity_number)
            self.add_building.click_on_next_button()
            self.log.info("*************** End the add building steep-1 **************")

            self.log.info("************** Start Add Building Step-2 ******************")
            self.file_path = XLUtils.readData(self.path, 'Sheet1', r, 8)
            self.building_type = XLUtils.readData(self.path, 'Sheet1', r, 9)
            self.construction_type = XLUtils.readData(self.path, 'Sheet1', r, 10)
            self.building_year = XLUtils.readData(self.path, 'Sheet1', r, 11)
            self.no_of_floors = XLUtils.readData(self.path, 'Sheet1', r, 12)
            self.no_of_parking_lots = XLUtils.readData(self.path, 'Sheet1', r, 13)
            self.add_building.add_building_step_2(self.file_path, self.building_type, self.construction_type, self.building_year,
                                                  self.no_of_floors, self.no_of_parking_lots)
            time.sleep(3)
            self.add_building.click_on_save_building_button()
            time.sleep(3)
            self.log.info("************** End Add Building Step-2 ******************")
            time.sleep(10)
            # Verifying the add building
            self.log.info("************** Start Add buildings verification ******************")
            actual_title = XLUtils.readData(self.path, 'Sheet1', r, 1)
            expected_title = self.add_building.verify_add_building(actual_title)
            if actual_title == expected_title:
                assert True
                self.driver.close()
            else:
                assert False

            self.log.info("************** Completed Add buildings verification ******************")

            

        
    
