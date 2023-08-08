# import pytest
# https://medium.com/testcult/intro-to-test-framework-pytest-5b1ce4d011ae
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException


def test_oodi_faq_interaction(browser):
    # GIVEN The Oodi homepage is displayed
    URL = "https://www.oodihelsinki.fi/en/"

    browser.get(URL)
    browser.implicitly_wait(20)

    # WHEN the user clicks on FAQ

    faq_search_window = browser.find_element(By.LINK_TEXT, "Questions and answers")

    browser.implicitly_wait(20)

    while True:
        try:
            faq_search_window.click()
            break
        except ElementClickInterceptedException:
            browser.execute_script("window.scrollBy(0,-100);")

    # THEN the FAQ page is displayed
    assert browser.current_url == "https://www.oodihelsinki.fi/en/faq/"

    browser.implicitly_wait(20)

    # AND the fact about dogs in the library is displayed
    xpath = "/html/body/div[1]/div[1]/div/div/section[2]/div[16]/div/div[1]/h3"

    def element_present_check():
        try:
            browser.find_element(By.XPATH, xpath)
            return True
        except NoSuchElementException:
            return False

    assert element_present_check() is True
