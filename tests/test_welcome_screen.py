import pytest
from screens.welcomeScreen import Welcome
from screens.login import Login

@pytest.mark.usefixtures('androidApp')


class TestWelcomeScreen:
    def test_sign_in_button(self):
        welcome = Welcome(self.driver)
        welcome.get_started_now_but()
        welcome.click_get_started_now_button()
        welcome.youtube_button()
        print("welcome to login screen")
