#!/usr/bin/env python
# coding: utf-8
import urllib
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
    print '请求地址:%s' % url
    html = response.read()
    return html


def get_content_by_post(url, cookie, args, login=False):
    """
    :param url:
    :param cookie:
    :param args:
    :param login:
    :return:
    """
    if login:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    else:
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', cookie))
    post_args = urllib.urlencode(args)
    response = opener.open(url, post_args)
    print 'POST请求地址:%s' % url
    html = response.read()
    return html
