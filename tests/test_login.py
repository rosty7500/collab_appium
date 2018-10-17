import pytest
from screens.welcomeScreen import Welcome
from screens.login import Login
from screens.loggedInHome import LoggedInHome


@pytest.mark.usefixtures('androidApp')
class TestLogin():
	def test_valid_login(self):
		welcome = Welcome(self.driver)
		login = Login(self.driver)
		loggedinhome = LoggedInHome(self.driver)
		
		welcome.sign_in_button()
		welcome.click_sign_in_button()
		login.fill_login_form("qaparesh1@gmail.com", "qa123123")
		login.click_submit()
		loggedinhome.logged_in_home()
