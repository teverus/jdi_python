from Pages.BaseElement import BaseElement
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, url="https://opensource-demo.orangehrmlive.com/"):
        super(LoginPage, self).__init__(driver, url)
        self.username_input = BaseElement('//*[@id="txtUsername"]', driver)
        self.password_input = BaseElement('//*[@id="txtPassword"]', driver)
        self.login_button = BaseElement('//*[@id="btnLogin"]', driver)
