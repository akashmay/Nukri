

import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):

    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    yield driver
    #driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser",
                     default="chrome",
                     action="store",
                     help="Commandline argument for adding required browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
