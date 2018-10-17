from screens.base import Base


class MyRides(Base):
	_my_rides_list = ('id', 'my_rides_listview')
	_my_ride_8_entry = ('xpath', '//android.widget.ListView/android.widget.RelativeLayout[8]')
	_my_ride_2_entry = ('xpath', '//android.widget.ListView/android.widget.RelativeLayout[2]')
	_upcoming_tab = ('id', 'my_rides_upcoming_textview')
	_ride_status = ('id', 'myride_single_status_textview')


	@property
	def ride_status_text(self):
		self.wait_visible(self._ride_status)
		ride_status_text = self.get_element_by_type('id', 'myride_single_status_textview')
		return ride_status_text.text

	def my_rides_list(self):
		self.wait_visible(self._my_rides_list)
		self.get_element(self._my_rides_list)

	def scroll_my_rides_list(self):
		self.swipe_to_element(self._my_rides_list, 'down')

	def click_upcoming_tab(self):
		self.wait_visible(self._upcoming_tab)
		self.click(self._upcoming_tab)
