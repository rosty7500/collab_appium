import pytest
import os
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


@pytest.fixture()
def androidApp(request):
    capabilities = {
        'platformName': 'Android',
        'platformVersion': '7.0',
        'appiumVersion': '1.6.1',
        'deviceName': 'ZY223ZJLQW',
        'appPackage': 'com.collabspace.collabspaceapp',
        'appActivity': 'com.collabspace.collabspaceapp.MainActivity',
        'autoGrantPermissions': 'true',
        "newCommandTimeout": 10
    }
    url = 'http://localhost:4723/wd/hub'
    request.instance.driver = webdriver.Remote(url, capabilities)

    def teardown():
        request.instance.driver.quit()
    request.addfinalizer(teardown)
