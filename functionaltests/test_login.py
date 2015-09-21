from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class LoginTest(FunctionalTest):

    def setUp(self):
        super().setUp()
        self.username = 'mark'
        self.password = 'password'
        self.user = User.objects.create_user(
            self.username, 'markscottwright@gmail.com', self.password)

    def test_user_can_login(self):

        # Mark opens our app
        self.browser.get(self.server_url + '/callog')

        # She notices the page title and that she needs to log in
        self.assertIn('Calories', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Please Log In', header_text)

        # Mark enters his name and password
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')

