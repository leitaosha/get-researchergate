# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/10/30  17:14
@Contact：473153250@qq.com
"""
import os
from datetime import datetime

from habanero import cn
import pandas as pd
import config

FileName = f"{config.ExportPath}{config.Url.split('/')[-1]} {datetime.now().strftime('%Y%m%d %H%M')}"


# CSV
def export_to_csv(articles: pd.DataFrame):
    """
    :param articles:
    """
    articles.to_csv(f"{FileName}.csv", index=False)


# XLSX
def export_to_xlsx(articles: pd.DataFrame):
    """
    :param articles:
    """
    articles.to_excel(f"{FileName}.xlsx", index=False)


# JSON
def export_to_json(articles: pd.DataFrame):
    """
    :param articles:
    """
    articles.to_json(f"{FileName}.json")


def export_to_markdown(articles: pd.DataFrame):
    """
    :param articles:
    """
    articles.to_markdown(f"{FileName}.md")


def export_to_bibtex(articles: pd.DataFrame):
    '''
    :param articles:
    :return:
    '''
    doiLs = articles['doi'].values.tolist()
    with open(FileName+".bib", 'a', encoding='utf-8') as f:
        f.write(''.join(list(cn.content_negotiation(doiLs, format='bibentry'))))


# 字符和函数的映射关系
export_functions = {
    'md': export_to_markdown,
    'xlsx': export_to_xlsx,
    'csv': export_to_csv,
    'json': export_to_json,
    'bibtex': export_to_bibtex,
}


def export(articles):
    """
    :param articles:
    """
    export_function = export_functions.get(config.Format)
    if export_function:
        export_function(articles)
