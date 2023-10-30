# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/10/30  20:18
@Contact：473153250@qq.com
"""
import re

DOI = re.compile(r'<meta property="citation_doi" content="(.*?)">')
Publication_Date = re.compile(r'<meta property="citation_publication_date" content="(.*?)">')
Publication = re.compile(r'<meta property="citation_journal_title" content="(.*?)s">')
First_Author = re.compile(r'<meta property="citation_author" content="(.*?)">')
DOI_URL = re.compile(r'<meta property="DC.identifier" content="(.*?)">')
Last_Author = re.compile(r'<meta property="citation_author" content="(.*?)">')
Title = re.compile(r'<meta property="citation_title" content="(.*?)">')
