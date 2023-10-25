# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/2/24  21:55
@Contact：473153250@qq.com
"""
import random
import re
import sys
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from tqdm import tqdm

articleLs = []  # 包含url字典的列表
authorUrlList = []  # 多余页面url 例如：/2   /3


def getTitle(browser: webdriver.chrome):
    """
    :param browser: 谷歌浏览器对象
    :param url: researchGate作者主页链接
    :return:
    """
    # XPATH空格需要用 . 代替
    lsParentXpath = '//div[@class="nova-legacy-o-stack nova-legacy-o-stack--gutter-xxl nova-legacy-o-stack--spacing-xl nova-legacy-o-stack--show-divider"]'
    elementListXpath = 'nova-legacy-o-stack__item'
    titleXpath = 'nova-legacy-e-link.nova-legacy-e-link--color-inherit.nova-legacy-e-link--theme-bare'
    # 显式等待：等待标签加载完毕
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    lsParent = browser.find_element(By.XPATH, lsParentXpath)
    # 每个条目列表
    elementList = lsParent.find_elements(By.CLASS_NAME, elementListXpath)
    for i in elementList:
        context = i.find_element(By.CLASS_NAME, titleXpath)
        infoUrl = context.get_attribute('href')
        title = context.text
        articleLs.append({"title": title, 'infoUrl': infoUrl, 'doi': ''})
    return articleLs


def getDOI(browser: webdriver.chrome):
    '''
    :param browser: 谷歌浏览器对象
    :return:
    '''
    # js
    num = 1
    for item in tqdm(articleLs, desc="请耐心等待...", unit="item", ncols=100):
        # 进度条
        num += 1
        # 格式 window.location.href="url"
        js = "window.location.href=" + '"' + f'{item["infoUrl"]}' + '"'
        browser.execute_script(js)
        time.sleep(0.5 + random.random())
        # meta data doi
        pattern = re.compile(r'<meta property="citation_doi" content="(.*?)">')
        results = pattern.findall(browser.page_source)
        if results:
            item['doi'] = results[0]
            # 获取作者
            # TODO 获取作者
    return articleLs


def getAuthorUrl(browser: webdriver.chrome, url: str):
    browser.get(url)
    time.sleep(4)
    getTitle(browser)
    try:
        pageElement = browser.find_element(By.CLASS_NAME,
                                           'nova-legacy-c-button-group.nova-legacy-c-button-group--wrap.nova-legacy-c-button-group--gutter-m.nova-legacy-c-button-group--orientation-horizontal.nova-legacy-c-button-group--width-auto')
        allPages = pageElement.find_elements(By.CLASS_NAME, 'nova-legacy-c-button-group__item')
        initPage = 1
        for page in allPages:
            if 2 <= initPage < len(allPages):
                url = page.find_element(By.TAG_NAME, 'a').get_attribute('href')
                authorUrlList.append(url)
            initPage += 1
        initPage = 0
        for url in authorUrlList:
            initPage += 1
            if initPage == 1:
                continue
            js = "window.location.href=" + '"' + f'{url}' + '"'
            browser.execute_script(js)
            time.sleep(4)
            getTitle(browser)
    except NoSuchElementException as e:
        print('仅有一页')
    print(f"检测到{len(articleLs)}个条目，获取doi中...")


def clickShowAllAuthor(chrome: webdriver.chrome):
    buttonShowAllAuthors = chrome.find_element(By.XPATH,
                                               '//*[@id="lite-page"]/main/section/section[1]/div/div/div[4]/div/span[1]/a')
    buttonShowAllAuthors.click()


def judgeFirstAuthor(chrome: webdriver.chrome, name: str):
    all_author = str(chrome.find_element(By.XPATH, '//*[@id="lite-page"]/main/section/section[1]/div/div/div[3]').text)
    if all_author.split('/n')[0] == name:
        return True
    return False


def authorNumber(chrome: webdriver.chrome, name: str):
    all_author = str(chrome.find_element(By.XPATH, '//*[@id="lite-page"]/main/section/section[1]/div/div/div[3]').text)
    author_list = all_author.split('/n')
    if len(all_author) > 0:
        return f"{author_list.index(name)} / {len(author_list)}"
    else:
        return None


def main(browser: webdriver.Chrome, url):
    print(f"目标网址：{url} 获取信息中...")
    getAuthorUrl(browser, url)
    return getDOI(browser)


if __name__ == '__main__':
    print(main())
