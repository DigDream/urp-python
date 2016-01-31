#!/usr/bin/env python
# coding: utf-8
import logging
from bs4 import BeautifulSoup
from utils.handlers.login import post_login
from utils.netutils import get_content_by_get
from utils.urls import URL_QUERY_GRADE

__author__ = 'qingfeng'


def query_grade(args):
    """
    :param args:
    :return:
    """
    cookie = args.cookie if args.cookie else None
    login = False
    # TODO 参数的互斥
    if cookie is None:
        cookie = post_login(args)
        login = True

    html_content = get_content_by_get(url=URL_QUERY_GRADE, cookie=cookie, login=login)
    html_content = unicode(html_content, "gb2312").encode("utf-8")
    soup = BeautifulSoup(html_content, 'html.parser')

    logging.info(soup.prettify())
