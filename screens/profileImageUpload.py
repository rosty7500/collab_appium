from screens.base import Base


class ProfileImage(Base):
    _profile_image = ('id', 'profile_profileimg')
    _select_from_gallery = ('id', 'profilelayout_takephotofromgallery')
    _images_folder = ('xpath', '//android.widget.RelativeLayout[@bounds="[0,408][1080,638]"]')
    _image_for_upload = ('accessibility_id', 'Photo taken on May 25, 2017 4:03:55 PM.')


    def click_profile_image(self):
        self.wait_visible(self._profile_image)
        self.click(self._profile_image)

    def gallery_button(self):
        self.wait_visible(self._select_from_gallery)

    def upload_file(self):
        self.click(self._select_from_gallery)
        self.wait_visible(self._images_folder)
        self.click(self._images_folder)
        self.wait_visible(self._image_for_upload)
        self.click(self._image_for_upload)
        self.wait_visible(self._profile_image)
