from screens.base import Base


class Homepage(Base):
    _map = ('accessibility_id', 'Google Map')
    _map_marker = ('id', 'book_my_ride_center_marker')


    def get_map(self):
        self.wait_visible(self._map)

    def map_marker(self):
        self.wait_visible(self._map_marker)
