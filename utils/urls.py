#!/usr/bin/env python
# coding: utf-8
from settings import URP_SITE

__author__ = 'qingfeng'

#   登录接口
URL_LOGIN = URP_SITE + 'loginAction.do'
#   获取验证码接口
URL_CAPTCHA = URP_SITE + 'validateCodeAction.do'
#   查询学籍接口
URL_ENROLLMENT_STATUS = URP_SITE + 'xjInfoAction.do?oper=xjxx'
#   本学期成绩
URL_QUERY_GRADE = URP_SITE + 'bxqcjcxAction.do'
#   及格成绩
URL_GRADE = URP_SITE + 'gradeLnAllAction.do?type=ln&oper=qbinfo'
#   评教列表
URL_EVALUATE_LIST = URP_SITE + 'jxpgXsAction.do?oper=listWj&pageSize=300'
#   具体评估
URL_EVALUATE_DETAIL = URP_SITE + 'jxpgXsAction.do?oper=wjpg'
#   评估界面
URL_EVALUATE = URP_SITE + 'jxpgXsAction.do'
