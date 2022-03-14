from time import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as _
from selenium.webdriver.support.wait import WebDriverWait

from constants import WAIT_FOR_ELEMENT


class BaseElement:
    def __init__(self, xpath, driver, name):
        self.driver = driver
        self.xpath = xpath
        self.name = name

    def _wait_until_element_appears(self):
        wait = WebDriverWait(self.driver, timeout=WAIT_FOR_ELEMENT)
        wait.until(_.visibility_of_element_located((By.XPATH, self.xpath)))

        return self.driver.find_element(By.XPATH, self.xpath)

    def _wait_until_element_value_is(self, target_value):
        element = self._wait_until_element_appears()

        wait = WebDriverWait(self.driver, timeout=WAIT_FOR_ELEMENT)
        wait.until(lambda d: element.get_attribute("value") == target_value)

    def _send_keys(self, keys):
        element = self._wait_until_element_appears()
        element.send_keys(keys)
        self._wait_until_element_value_is(keys)

    def _click(self):
        start_time = time()
        element = self._wait_until_element_appears()
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        finish_time = round(time() - start_time, 1)
        print(
            f"""[{finish_time} s] Clicking "{self.name.replace('_', ' ')}" ({self.xpath})"""
        )

    def _is_visible(self):
        start_time = time()
        finish_time = round(time() - start_time, 1)
        self._wait_until_element_appears()
        print(
            f"""[{finish_time} s] Waiting until "{self.name.replace('_', ' ')}" ({self.xpath}) is visible"""
        )
