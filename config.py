# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/2/25  19:43
@Contact：473153250@qq.com
"""
import os

# Replace this url that you want to crawl
Url = 'https://www.researchgate.net/profile/Leitao-Sha'

# Export format. support for xlsx / md / csv / json
Format = 'xlsx'


# ROOT PATH
rootPath = os.path.dirname(os.path.realpath(__file__))

# chrome.exe
Chrome_Binary_Location = rootPath + r"\chrome\chrome.exe"

# chromedriver
Chrome_Driver_Path = rootPath + r"\chromedriver\chromedriver.exe"

# export path
ExportPath = rootPath + r"\\DATA\\"
