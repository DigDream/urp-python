#!/usr/bin/env python
# coding: utf-8
import argparse

__author__ = 'qingfeng'


def parse_argv():
    """
    :return:
    """

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='sub-command help', dest='mode')

    #   查询成绩
    ccj_parser = subparsers.add_parser('grade', help='query_grade')
    ccj_parser.add_argument('-no', dest='number', type=str, default=False, help='student number')
    ccj_parser.add_argument('-cookie', dest='cookie', type=str, default=False, help='test')

    #   查询课表

    #   一键评估
    yjpg_parser = subparsers.add_parser('yjpg', help='yijianpinggu')
    yjpg_parser.add_argument('-no', dest='number', type=str, default=False, help='student number')
    yjpg_parser.add_argument('-cookie', dest='cookie', type=str, default=False, help='test')

    #   学籍查询
    status_parser = subparsers.add_parser('status', help='status')
    status_parser.add_argument('-no', dest='number', type=str, default=False, help='student number')
    status_parser.add_argument('-cookie', dest='cookie', type=str, default=False, help='test')

    #   登录接口
    ccj_parser = subparsers.add_parser('login', help='login')
    ccj_parser.add_argument('-no', dest='number', type=str, default=False, help='student number')

    return parser.parse_args()
