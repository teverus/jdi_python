from selenium.webdriver.support.wait import WebDriverWait

from Pages.BaseElement import BaseElement
from constants import WAIT_FOR_ELEMENT


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.logo = BaseElement('//*[@id="branding"]/a[1]/img', self.driver)

    def open(self):
        self.driver.get(self.url)
        self.wait_until_current_url_is(self.url)

    def wait_until_current_url_is(self, target_url):
        wait = WebDriverWait(self.driver, timeout=WAIT_FOR_ELEMENT)
        wait.until(lambda d: d.current_url == target_url)
