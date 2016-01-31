#!/usr/bin/env python
# coding: utf-8
import logging
from bs4 import BeautifulSoup
from settings import EVALUATE_CONTENT
from settings import EVALUATE_RADIO_CONTENT
from utils.handlers.login import post_login
from utils.netutils import get_content_by_get
from utils.netutils import get_content_by_post
from utils.urls import URL_EVALUATE_LIST
from utils.urls import URL_EVALUATE_DETAIL
from utils.urls import URL_EVALUATE

__author__ = 'qingfeng'


def evaluate_teacher(args):
    """
    :param args:
    :return:
    """
    cookie = args.cookie if args.cookie else None
    login = False
    if cookie is None:
        cookie = post_login(args)
        login = True

    html_content = get_content_by_get(url=URL_EVALUATE_LIST, cookie=cookie, login=login)
    html_content = unicode(html_content, "gb2312").encode("utf-8")
    soup = BeautifulSoup(html_content, 'html.parser')

    logging.info(soup.prettify())
    evaluate_list = soup.find_all('tr', class_="odd")
    for i in evaluate_list:
        if i.contents[7].string == u'否':
            # print i.contents[9].img.attrs['name']
            post_data = {"wjbm": i.contents[9].img.attrs['name'][:10], "bpr": i.contents[9].img.attrs['name'][12:19],
                         "pgnr": i.contents[9].img.attrs['name'][-8:], "oper": "wjShow"}
            post_result = get_content_by_post(URL_EVALUATE, cookie, post_data, login)
            post_result = unicode(post_result, "gb2312").encode("utf-8")
            logging.info(post_result)

            data = {"wjbm": i.contents[9].img.attrs['name'][:10], "bpr": i.contents[9].img.attrs['name'][12:19],
                    "pgnr": i.contents[9].img.attrs['name'][-8:], "xumanyzg": "zg", "wjbz": "",
                    "zgpj": EVALUATE_CONTENT, "0000000003": EVALUATE_RADIO_CONTENT}
            for j in range(5, 8):
                data['000000000%s' % j] = EVALUATE_RADIO_CONTENT
            for j in range(26, 29):
                data['00000000%s' % j] = EVALUATE_RADIO_CONTENT
            for j in range(35, 38):
                data['00000000%s' % j] = EVALUATE_RADIO_CONTENT
            result = get_content_by_post(URL_EVALUATE_DETAIL, cookie, data, login)
            result = unicode(result, "gb2312").encode("utf-8")
            logging.info(result)
