from selenium.webdriver.common.by import By

# from selenium.common.exceptions import ElementClickInterceptedException


def test_oodi_facilities_interaction(browser):
    # Given The Oodi homepage is displayed
    URL = "https://www.oodihelsinki.fi/en/"

    browser.get(URL)
    browser.implicitly_wait(20)

    # WHEN the user clicks the plus buttton to expand 'Services and facilities'
    # AND the user clicks on 'facilities'

    plus_button_xpath = (
        "/html/body/section/div[1]/div[1]/nav/ul/li[2]/button/div/div[2]"
    )
    facilities_xpath = "/html/body/section/div[1]/div[1]/nav/ul/li[2]/ul/li/ul/li[2]/a"

    browser.implicitly_wait(20)

    plus_button = browser.find_element(By.XPATH, plus_button_xpath)
    plus_button.click()
    browser.implicitly_wait(20)
    facilities = browser.find_element(By.XPATH, facilities_xpath)
    facilities.click()
    browser.implicitly_wait(20)

    # THEN the user is on the facilities page

    assert (
        browser.current_url
        == "https://www.oodihelsinki.fi/en/services-and-facilities/facilities/"
    )
