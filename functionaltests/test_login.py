from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User


class LoginTest(FunctionalTest):

    def setUp(self):
        super().setUp()
        self.username = 'mark'
        self.password = 'password'
        self.user = User.objects.create_user(
            self.username, 'markscottwright@gmail.com', self.password)

    def test_bad_credentials_cant_login(self):

        # Hacker opens our app
        self.browser.get(self.server_url + '/callog')

        # Hacker enters a fake name and password
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('mark')
        password.send_keys('badpassword' + Keys.RETURN)

        # The login fails
        body = self.browser.find_element_by_tag_name('body').text
        self.assertIn(
            "Your username and password didn't match", body)

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
        username.send_keys('mark')
        password.send_keys('password' + Keys.RETURN)

        # Mark is successfully logged in
        body = self.browser.find_element_by_tag_name('body').text
        self.assertIn("hello", body)

    def test_user_can_logout(self):

        # Mark opens our app
        self.browser.get(self.server_url + '/callog')

        # Mark enters his name and password
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('mark')
        password.send_keys('password' + Keys.RETURN)

        # Mark then navigates to the logout page
        self.browser.get(self.server_url + '/accounts/logout')

        # He sees a logout message
        body = self.browser.find_element_by_tag_name('body').text
        self.assertIn("You've been logged out", body)

        # He then goes back to the main page and is prompted for a login again
        self.browser.get(self.server_url + '/callog')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Please Log In', header_text)
