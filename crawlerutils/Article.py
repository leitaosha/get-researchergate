# -*- coding: utf-8 -*-
"""
@Author：ForSmile
@Time：2023/10/30  17:19
@Contact：473153250@qq.com
"""


# fields of article

class Article:
    """
    fields of article
    """

    def __init__(self, title=None, authors=None, publication=None, date=None, doi=None, abstract=None, gateUrl=None,
                 doiUrl=None, lastAuthor=None):
        # fields
        self.title = title
        self.doi = doi
        self.authors = authors
        self.firstAuthor = authors[0] if authors is not None else None
        self.lastAuthor = lastAuthor
        self.publication = publication
        self.date = date
        self.abstract = abstract
        self.gateUrl = gateUrl
        self.doiUrl = doiUrl

