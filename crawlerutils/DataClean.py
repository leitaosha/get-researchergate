# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/10/31  22:29
@Contact：473153250@qq.com
"""
import pandas as pd

import config
from crawlerutils.Register import Register

registerFunc = Register()

@registerFunc
def publicationFilter(data: pd.DataFrame):
    return data[~data['publication'].isin(config.Field['publication'])]


@registerFunc
def doiFilter(data: pd.DataFrame):
    return data[~data['doi'].isin(config.Field['doi'])]


def clean_data(df: pd.DataFrame):
    print('数据清洗...')
    for func in registerFunc.values():
        df = func(df)
    return df
