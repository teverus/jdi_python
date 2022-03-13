from Pages.DashboardPage import DashboardPage
from Pages.LoginPage import LoginPage


class WebSite:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver)
