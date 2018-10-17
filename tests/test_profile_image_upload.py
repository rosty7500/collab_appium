import pytest
from screens.welcomeScreen import Welcome
from screens.login import Login
from screens.loggedInHome import LoggedInHome
from screens.loggedInSideMenu import SideMenu
from screens.profileImageUpload import ProfileImage


@pytest.mark.usefixtures('androidApp')
class TestProfileImageUpload:
    def test_profile_image_upload(self):
        welcome = Welcome(self.driver)
        login = Login(self.driver)
        loggedinhome = LoggedInHome(self.driver)
        sidemenu = SideMenu(self.driver)
        profileImage = ProfileImage(self.driver)

        welcome.sign_in_button()
        welcome.click_sign_in_button()

        login.fill_login_form("qaparesh1@gmail.com", "qa123123")
        login.click_submit()

        loggedinhome.logged_in_home()

        sidemenu.click_top_menu_button()
        sidemenu.click_profile_image()

        profileImage.click_profile_image()
        profileImage.gallery_button()
        profileImage.upload_file()
