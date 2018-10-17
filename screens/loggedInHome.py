from screens.base import Base


class LoggedInHome(Base):
	_book_navigation_address_field = ('id', 'book_navigation_address_layout')


	def logged_in_home(self):
		self.wait_visible(self._book_navigation_address_field)
