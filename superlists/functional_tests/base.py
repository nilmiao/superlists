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

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > self.MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                self.check_for_row_in_list_table(row_text)
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > self.MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])