#!/usr/bin/env python
# coding: utf-8
import cookielib
import getpass
import logging
import urllib
import urllib2
from utils.urls import URL_CAPTCHA, URL_LOGIN

__author__ = 'qingfeng'

"""
about login
"""

cookie = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))


def get_captcha():
    """
    :return:
    """
    img_content = opener.open(URL_CAPTCHA).read()
    captcha = open('image.jpg', 'wb')
    captcha.write(img_content)
    captcha.close()


def post_login(args):
    """
    :return:
    """
    get_captcha()
    password = getpass.getpass('password:')
    captcha = raw_input("captcha: ")
    data = {"zjh": args.number, "mm": password, "v_yzm": captcha}
    post_info = urllib.urlencode(data)
    request = urllib2.Request(URL_LOGIN, post_info)
    html = opener.open(request).read()
    html = unicode(html, "gb2312").encode("utf-8")
    # TODO 返回的判断
    logging.info(html)
    return cookie
