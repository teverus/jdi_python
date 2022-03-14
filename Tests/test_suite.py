from Pages.BaseElement import BaseElement
from Pages.BasePage import BasePage


def test_ireland(driver):
    Irish_website = BasePage(driver, url="https://www.kdmid.ru/docs.aspx")._open()
    consulate_functions_button = BaseElement(
        "//*[@id='button_cons2']/a", driver, "consulate_functions_button"
    )._click()
    get_a_passport_button = BaseElement(
        "//*[@id='nav']/ul/li[2]/a", driver, "get_a_passport_button"
    )._is_visible()


def test_racoon(driver):
    a_web_page = BasePage(driver, url="https://vot-enot.com/")._open()
    rules_button = BaseElement(
        "//*[@id='menu-item-538']/a/span", driver, "rules_button"
    )._click()
    rules_title = BaseElement(
        "//*[@id='main']/header/div/h1", driver, "rules_title"
    )._is_visible()
