from pageObject.Building_Home import AddHome
from pageObject.Login_page import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class TestAddHomeWithDDT:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGen.custom_logger()
    path = ".//TestData/add_home_ddt.xlsx"

    def test_add_home_by_xlsx(self, setup):
        self.log.info("************* Test_Add_Home **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        # self.log.info("************* Starting Login *************")
        # login.login_test()
        # self.log.info("************* Login successful **********")

        self.log.info("************* Starting Login *************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.log.info("************* Login successful **********")

        self.add_home = AddHome(self.driver)
        self.add_home.click_add_home_lnk()
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        for r in range(2, self.rows + 1):
            self.add_home.click_add_home_lnk()
            self.log.info("************ Start The Add Building Step-1 ********** ")
            self.building_title = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.house_number = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.add_home.select_building_selector(self.building_title)
            self.add_home.add_home_number(self.house_number)
            self.add_home.click_add_home_button()
            self.add_home.click_save_button()

