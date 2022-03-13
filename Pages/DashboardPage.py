from Pages.BasePage import BasePage


class DashboardPage(BasePage):
    def __init__(
        self,
        driver,
        url="https://opensource-demo.orangehrmlive.com/index.php/dashboard",
    ):
        super(DashboardPage, self).__init__(driver, url)
