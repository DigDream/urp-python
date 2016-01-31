#!/usr/bin/env python
# coding: utf-8
import logging
from bs4 import BeautifulSoup
from utils.handlers.login import post_login
from utils.netutils import get_content_by_get
from utils.urls import URL_ENROLLMENT_STATUS

__author__ = 'qingfeng'


def query_enrollment_status(args):
    """
    :param args:
    :return:
    """
    # TODO 关于复用
    # TODO 异常的处理
    cookie = args.cookie if args.cookie else None
    login = False
    if cookie is None:
        cookie = post_login(args)
        login = True

    html_content = get_content_by_get(url=URL_ENROLLMENT_STATUS, cookie=cookie, login=login)
    soup = BeautifulSoup(html_content, 'html.parser')
    logging.info(soup.prettify())
