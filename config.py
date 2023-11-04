# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/2/25  19:43
@Contact：473153250@qq.com
"""
import os

# Replace this url that you want to crawl
Url = 'https://www.researchgate.net/profile/Leitao-Sha'

# Export format. support for xlsx / md / csv / json / bibtex
Format = 'bibtex'

# ROOT PATH
rootPath = os.path.dirname(os.path.realpath(__file__))

# Chrome Option
isAutoChromeDriver = False

# chrome.exe
Chrome_Binary_Location = rootPath + r"\chrome\chrome.exe"

# chromedriver
Chrome_Driver_Path = rootPath + r"\chromedriver\chromedriver.exe"

# export path
ExportPath = rootPath + r"\\DATA\\"

# Data Clean
isDataClean = True

CleanField = {
    'publication': ['SSRN Electronic Journal', ''],
    # exclude some useless data, such as ["SSRN Electronic Journal", "..."]
    'doi': [],
}
