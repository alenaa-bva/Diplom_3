import pytest
from selenium import webdriver


@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture()
def firefox():
    driver = webdriver.Firefox()
    return driver

@pytest.fixture(params=["chrome", "firefox"])
def driver(request, chrome, firefox):
    if request.param == 'chrome':
        DRIVER_NAME = 'chrome'
        webdriver = chrome
        webdriver.maximize_window()
        firefox.quit()
    else:
        DRIVER_NAME = 'firefox'
        webdriver = firefox
        webdriver.maximize_window()
        chrome.quit()

    yield webdriver
    webdriver.quit()
