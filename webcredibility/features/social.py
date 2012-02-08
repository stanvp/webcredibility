# -*- coding: utf-8 -*-

from webcredibility.util import pagerank

def page_rank(document):
    return {
        "@page_rank": pagerank.get_pagerank(document.url)
    }