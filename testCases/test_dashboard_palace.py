import time
from pageObject.Login_page import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObject.Dashboard_page import Dashboard


class Test_004_Dashboard_Palace:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGen.custom_logger()

    def test_dashboard_palace(self, setup):
        self.log.info("************* Test_004 Dashboard **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.log.info("************* Starting Login *************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.log.info("************* Login successful **********")

        self.log.info("************* Starting Dashboard Palace **********")
        self.dashboard_palace = Dashboard(self.driver)
        # time.sleep(8)
        # self.dashboard_link.get_all_links()
        self.water = self.dashboard_palace.get_water_name()
        print(self.water)
        self.hub = self.dashboard_palace.get_hub_name()
        print(self.hub)
        self.fire = self.dashboard_palace.get_fire_name()
        print(self.fire)
        self.alarm = self.dashboard_palace.get_alarm_name()
        print(self.alarm)
        if self.water == "Water" and self.hub == "Hub" and self.fire == "Fire" and self.alarm == "Alarm":
            assert True
            self.driver.close()
        else:
            assert False
