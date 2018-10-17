import pytest
from screens.welcomeScreen import Welcome
from screens.login import Login
from screens.loggedInHome import LoggedInHome
from screens.loggedInSideMenu import SideMenu
from screens.myRides import MyRides


@pytest.mark.usefixtures('androidApp')
class TestMyRides:
	def test_my_rides_list_scroll(self):
		welcome = Welcome(self.driver)
		login = Login(self.driver)
		loggedinhome = LoggedInHome(self.driver)
		sidemenu = SideMenu(self.driver)
		myrides = MyRides(self.driver)

		welcome.sign_in_button()
		welcome.click_sign_in_button()

		login.fill_login_form("qaparesh1@gmail.com", "qa123123")
		login.click_submit()

		loggedinhome.logged_in_home()

		sidemenu.click_top_menu_button()
		sidemenu.click_my_rides_button()

		myrides.my_rides_list()
		myrides.scroll_my_rides_list()

	def test_upcoming_rides_statuses(self):
		welcome = Welcome(self.driver)
		login = Login(self.driver)
		loggedinhome = LoggedInHome(self.driver)
		sidemenu = SideMenu(self.driver)
		myrides = MyRides(self.driver)

		welcome.sign_in_button()
		welcome.click_sign_in_button()

		login.fill_login_form("qaparesh1@gmail.com", "qa123123")
		login.click_submit()

		loggedinhome.logged_in_home()

		sidemenu.click_top_menu_button()
		sidemenu.click_my_rides_button()

		myrides.my_rides_list()
		myrides.click_upcoming_tab()
		myrides.my_rides_list()
		assert myrides.ride_status_text == "Accepted"
