from time import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BaseElement import BaseElement
from constants import WAIT_FOR_ELEMENT


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.logo = BaseElement('//*[@id="branding"]/a[1]/img', self.driver, "logo")

    def _open(self):
        start_time = time()
        self.driver.get(self.url)
        self._wait_until_current_url_is(self.url)
        finish_time = round(time() - start_time, 1)
        print(f"[{finish_time} s] Opening {self.url} ")

    def _wait_until_current_url_is(self, target_url):
        wait = WebDriverWait(self.driver, timeout=WAIT_FOR_ELEMENT)
        try:
            wait.until(lambda d: d.current_url == target_url)
        except TimeoutException:
            raise TimeoutException(
                f"\n[ERROR] Expected {self.driver.current_url} to be {target_url}"
            )
