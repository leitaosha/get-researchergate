# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/10/30  17:14
@Contact：473153250@qq.com
"""
import os
from datetime import datetime
import pandas as pd
import config

ProjectPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
outPath = ProjectPath + "\\DATA\\"

FileName = f"{outPath}{config.Url.split('/')[-1]} {datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"




# CSV
def export_to_csv(articles):
    """
    :param articles:
    """
    data = [vars(each) for each in articles]
    df = pd.DataFrame(data)
    df.to_csv(f"{FileName}.csv", index=False)


# XLSX
def export_to_xlsx(articles):
    """
    :param articles:
    """
    data = [vars(each) for each in articles]
    df = pd.DataFrame(data)
    df.to_excel(f"{FileName}.xlsx", index=False)


# JSON
def export_to_json(articles):
    """
    :param articles:
    """
    data = [vars(each) for each in articles]
    df = pd.DataFrame(data)
    df.to_json(f"{FileName}.json")


def export_to_markdown(articles):
    """
    :param articles:
    """
    data = [vars(each) for each in articles]
    df = pd.DataFrame(data)
    df.to_markdown(f"{FileName}.md")


# 字符和函数的映射关系
export_functions = {
    'md': export_to_markdown,
    'xlsx': export_to_xlsx,
    'csv': export_to_csv,
    'json': export_to_json,
}


def export(articles):
    """
    :param articles:
    """
    export_function = export_functions.get(config.Format)
    if export_function:
        export_function(articles)