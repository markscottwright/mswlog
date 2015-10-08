from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys
import time


class FunctionalTest(StaticLiveServerTestCase):

    SELENIUM_PROFILE = r'C:\Users\wrightm\AppData\Roaming\mozilla\firefox\profiles\o0a8hsna.selenium'

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        profile = webdriver.firefox.firefox_profile.FirefoxProfile(
            self.SELENIUM_PROFILE)
        self.browser = webdriver.Firefox(profile)
        self.browser.implicitly_wait(3)

    def closeBrowser(self):
        # this works around a bug that throws an exception in the django
        # webserver
        time.sleep(1)
        self.browser.refresh()
        self.browser.quit()

    def tearDown(self):
        self.closeBrowser()
