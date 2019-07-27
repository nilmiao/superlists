# -*- coding: utf-8 -*-
# Created by nil_mmm
import time
from .base import FunctionlTest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


class ItemValidationTest(FunctionlTest):
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # 提示待办事项不能为空
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        # 输入一些文字，然后再次提交
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_itme').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # 又提交了一个空事项
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        # 输入文字之后就没问题了
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
