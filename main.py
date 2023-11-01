# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/2/25  20:12
@Contact：473153250@qq.com
"""
import pandas as pd

from crawlerutils import ChromeBrowser as cb
from crawlerutils import AuthorArtical as aa
import config
import crawlerutils.ExportFormat as export
from crawlerutils.DataClean import clean_data


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
    # 作者主页
    url = config.Url
    # 获取数据
    articles = getAuthorPaper(url)
    # 转为pd.DataFrame
    articles = pd.DataFrame([vars(each) for each in articles])
    # 数据清洗
    articles = clean_data(articles)
    # 信息导出
    export.export(articles)
    # 信息提示
    print('写入文件完成！！！')
