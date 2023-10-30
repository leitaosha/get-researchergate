# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/2/25  20:12
@Contact：473153250@qq.com
"""

from crawlerutils import ChromeBrowser as cb
from crawlerutils import AuthorArtical as aa
from datetime import datetime
import config as CONFIG
import crawlerutils.ExportFormat as export


def getAuthorPaper(url: str):
    '''
    :param url: such as 'https://www.researchgate.net/profile/authorName'
    :return:
    '''
    obj = cb.ChromeBrowser()
    with obj:
        chrome = obj.Browser
        articles = aa.main(chrome, url)
    return articles


if __name__ == '__main__':
    #作者主页
    url = CONFIG.Url
    articles = getAuthorPaper(url)
    export.export(articles)
    print('写入文件完成！！！')

