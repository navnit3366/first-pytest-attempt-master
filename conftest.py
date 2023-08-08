# Thanks to PyBites
# https://pybit.es/pytest-fixtures.html
# setup and teardown in own file. I did need to sope to module... .

import pytest

from selenium.webdriver import Chrome

# Initialize and quit handled by a pytest fixture
@pytest.fixture
def browser(scope="module"):
    driver = Chrome()

    driver.implicitly_wait(15)
    yield driver
    driver.quit()
