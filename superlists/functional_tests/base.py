# -*- coding: utf-8 -*-
# Created by nil_mmm
import time
from unittest import skip
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os


class FunctionlTest(StaticLiveServerTestCase):
    def setUp(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('--headless')
        self.option.add_argument('--no-sandbox')
        self.option.add_argument('--disable-extensions')
        self.option.add_argument('--disable-gpu')
        self.option.add_argument('--disable-dev-shm-usage')
        # self.browser = webdriver.Chrome('/home/chromedriver',chrome_options=self.option)
        self.browser = webdriver.Chrome(chrome_options=self.option)
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        self.MAX_WAIT = 10

    def tearDown(self):
        self.browser.quit()