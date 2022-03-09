import time
from pageObject.Login_page import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObject.Dashboard_page import Dashboard


class TestDashboardQuickAccessConnectDevicesToHome:
    log = LogGen.custom_logger()
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    expected_url = "https://dev.portal.abrahome.com/devices"

    def test_dashboard_quick_access_connect_devices_to_home(self, setup):
        self.log.info("************* Test_007 Dashboard **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        # Login Here
        self.log.info("************* Starting Login *************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.log.info("************* Login succesful **********")
        time.sleep(10)
        self.log.info("************* Starting Dashboard Quick_Access Connect_Devices_To_Home **********")
        self.dashboard_quick_access = Dashboard(self.driver)
        self.dashboard_quick_access.click_on_connect_devices_img_btn()
        time.sleep(4)
        current_url = self.driver.current_url
        print("The current url is:", current_url)
        print("Expected url:", self.expected_url)
        if current_url == self.expected_url:
            time.sleep(3)
            assert True
            self.driver.close()
            
        else:
            self.log.info("Open URL not correct")
            assert False
        self.log.info("************* Finished Dashboard Quick_Access Connect_Devices_To_Home**********")