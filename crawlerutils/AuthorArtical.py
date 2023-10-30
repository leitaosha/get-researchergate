# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/2/24  21:55
@Contact：473153250@qq.com
"""
import random
import re
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from tqdm import tqdm

from crawlerutils import Regex
from crawlerutils.Article import Article

articles = [Article(date=12)]
articles.clear()  # 包含url字典的列表
authorUrlList = []  # 多余页面url 例如：/2   /3


class InfoCrawler:
    """
    crawl info
    """

    def __init__(self, browser: webdriver.chrome):
        self.articles = articles
        self.browser = browser

    def run(self):
        """
            执行函数
        """
        # js
        for item in tqdm(self.articles, desc="请耐心等待...", unit="item", ncols=100):
            # 格式 window.location.href="url"
            js = "window.location.href=" + '"' + f'{item.gateUrl}' + '"'
            self.browser.execute_script(js)
            time.sleep(0.3 + random.random())
            # 获取各个字段
            item.doi = self.getDOI()
            item.publication = self.getPublication()
            item.date = self.getPublicationDate()
            item.firstAuthor = self.getFirstAuthor()
            item.doiUrl = self.getDoiUrl()
            item.title = self.getTitle()
            item.lastAuthor = self.getLastAuthor()

        global articles
        articles = self.articles

    def getDOI(self):
        # meta data doi
        results = Regex.DOI.findall(self.browser.page_source)
        return results[0] if results else ''

    def getTitle(self):
        # meta data doi
        results = Regex.Title.findall(self.browser.page_source)
        return results[0] if results else ''

    def getFirstAuthor(self):
        results = Regex.First_Author.findall(self.browser.page_source)
        return results[0] if results else ''

    def getLastAuthor(self):
        results = Regex.Last_Author.findall(self.browser.page_source)
        return results[-1] if results else ''
    def getDoiUrl(self):
        results = Regex.DOI_URL.findall(self.browser.page_source)
        return results[0] if results else ''

    def getPublication(self):
        publication = ''
        try:
            el = self.browser.find_element(By.CLASS_NAME,
                                           "nova-legacy-e-link.nova-legacy-e-link--color-inherit."
                                           "nova-legacy-e-link--theme-decorated")
            publication = el.text
        except NoSuchElementException:
            pass
        return publication

    def getPublicationDate(self):
        results = Regex.Publication_Date.findall(self.browser.page_source)
        return results[0] if results else ''

    def clickShowAllAuthor(self):
        buttonShowAllAuthors = self.browser.find_element(By.XPATH,
                                                         '//*[@id="lite-page"]/main/section/section[1]/div/div/div[4]/div/span[1]/a')
        buttonShowAllAuthors.click()

    def judgeFirstAuthor(self, name: str):
        all_author = str(
            self.browser.find_element(By.XPATH, '//*[@id="lite-page"]/main/section/section[1]/div/div/div[3]').text)
        if all_author.split('/n')[0] == name:
            return True
        return False

    def authorNumber(self, name: str):
        all_author = str(
            self.browser.find_element(By.XPATH, '//*[@id="lite-page"]/main/section/section[1]/div/div/div[3]').text)
        author_list = all_author.split('/n')
        if len(all_author) > 0:
            return f"{author_list.index(name)} / {len(author_list)}"
        else:
            return None


# 获取单页面每个条目的url和标题
def getPerPageArticleUrl(browser: webdriver.chrome):
    """
    :param browser: 谷歌浏览器对象
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
        articles.append(Article(gateUrl=infoUrl))


# 获取可能多个页面所有的ulr和标题
def getAuthorUrl(browser: webdriver.chrome, url: str):
    """
    :param browser:
    :param url: 作者主页url
    """
    browser.get(url)
    time.sleep(4)
    getPerPageArticleUrl(browser)
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
            getPerPageArticleUrl(browser)
    except NoSuchElementException as e:
        print('仅有一页')
    print(f"检测到{len(articles)}个条目，获取信息中...")


def main(browser: webdriver.Chrome, url):
    """
    :param browser:
    :param url:
    """
    print(f"目标网址：{url} 获取信息中...")
    getAuthorUrl(browser, url)
    InfoCrawler(browser).run()
    return articles
