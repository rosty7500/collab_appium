from screens.base import Base


class Welcome(Base):
    get_started_now_button = ('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]')
    youtube_login_button = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.support.v4.view.ViewPager/android.view.ViewGroup/android.view.ViewGroup[1]')

    def get_started_now_but(self):
        self.wait_visible(self.get_started_now_button)

    def click_get_started_now_button(self):
        self.click(self.get_started_now_button)

    def youtube_button(self):
        self.wait_visible(self.youtube_login_button)


