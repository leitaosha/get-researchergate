# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/2/27  19:25
@Contact：473153250@qq.com
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config


class ChromeBrowser:

    def __init__(self):
        # 浏览器配置
        self.__BROWSER_HEAD = True
        self.__BROWSER_IMAGE = False
        self.__BROWSER_CSS = False
        self.__options = Options()
        # 浏览器对象
        self.__BROWSER = None
        # 浏览器路径
        # self.__options.binary_location = config.Chrome_Binary_Location

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__BROWSER is None:
            return
        else:
            self.__BROWSER.close()
            print('{:-^50}'.format('浏览器已关闭！'))

    def __enter__(self):
        print("进入浏览器")
        if not self.__BROWSER_HEAD:
            self.__options.add_argument("--headless")
            self.__options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/95.0.4638.69 Safari/537.36")
            self.__options.add_argument('window-size=1920x1080')
            self.__options.add_argument('--start-maximized')
        # 禁用image、css
        prefs = {}
        if not self.__BROWSER_IMAGE:
            prefs['profile.managed_default_content_settings.images'] = 2
        if not self.__BROWSER_CSS:
            prefs['permissions.default.stylesheet'] = 2
        self.__options.add_experimental_option("prefs", prefs)

    @property
    def Browser(self):
        self.__BROWSER = webdriver.Chrome(self.__options)
        return self.__BROWSER
