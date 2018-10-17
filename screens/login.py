from screens.base import Base


class Login(Base):
	_email_field = ('id', 'login_email_editText')
	_password_field = ('id', 'login_password_editText')
	_login_submit_button = ('id', 'login_submit_button')


	def email_field(self):
		self.wait_visible(self._email_field)

	def password_field(self):
		self.wait_visible(self._password_field)

	def type_email(self, value):
		self.wait_visible(self._email_field).send_keys(value)

	def type_password(self, value):
		self.wait_visible(self._password_field).send_keys(value)

	def fill_login_form(self, email, password):
		self.type_email(email)
		self.type_password(password)

	def click_submit(self):
		self.click(self._login_submit_button)
