from screens.base import Base


class SideMenu(Base):
	_top_menu_button = ('id', 'book_navigation_layout')
	_profile_icon = ('id', 'profile_icon')
	_my_rides_button = ('xpath', '//android.widget.ListView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout[@resource-id="com.moovn.rider:id/drawer_list_item_normal_layout"]')


	def click_top_menu_button(self):
		self.wait_visible(self._top_menu_button)
		self.click(self._top_menu_button)

	def click_my_rides_button(self):
		self.wait_visible(self._my_rides_button)
		self.click(self._my_rides_button)

	def click_profile_image(self):
		self.wait_visible(self._profile_icon)
		self.click(self._profile_icon)
