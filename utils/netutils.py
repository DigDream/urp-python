#!/usr/bin/env python
# coding: utf-8
import urllib2

__author__ = 'qingfeng'


def get_content_by_get(url, cookie, login=False):
    """
    :param url:
    :param cookie:
    :param login:
    :return:html
    """
    if login:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    else:
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', cookie))
    response = opener.open(url)
    # response = urllib2.urlopen(url)
    print url
    html = response.read()
    return html
