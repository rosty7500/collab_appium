import pytest
from screens.welcomeScreen import Welcome
from screens.login import Login
from screens.loggedInHome import LoggedInHome
from screens.homepage import Homepage


@pytest.mark.usefixtures('androidApp')
class TestHomepage:
    def test_map(self):
        welcome = Welcome(self.driver)
        login = Login(self.driver)
        loggedinhome = LoggedInHome(self.driver)
        homepage = Homepage(self.driver)

        welcome.sign_in_button()
        welcome.click_sign_in_button()

        login.fill_login_form("qaparesh1@gmail.com", "qa123123")
        login.click_submit()

        loggedinhome.logged_in_home()

        homepage.get_map()
        homepage.map_marker()
