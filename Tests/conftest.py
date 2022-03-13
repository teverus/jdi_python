import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Pages.WebSite import WebSite


@pytest.fixture(autouse=True)
def driver():
    # Make WebDriver save a driver executable in the root directory of the project
    os.environ["WDM_LOCAL"] = "1"

    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1080")

    # Remove Chrome browser debugging info from the console
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(log_level=0).install()), options=options
    )

    yield driver

    driver.quit()


@pytest.fixture()
def _(driver):
    return WebSite(driver)
