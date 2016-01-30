#!/usr/bin/env python
# coding: utf-8
import logging
import sys
import signal
from utils.handlers.evaluate import evaluate_teacher

from utils.handlers.grade import query_grade
from utils.handlers.status import query_enrollment_status
from utils.parse.cli import parse_argv

__author__ = 'qingfeng'


def main():
    """
    :return:
    """
    logging.basicConfig(filename='urp.log', level=logging.INFO)
    logging.info('Program Started')
    args = parse_argv()

    if args.mode == 'status':
        query_enrollment_status(args)
    elif args.mode == 'grade':
        query_grade(args)
    elif args.mode == 'yjpg':
        evaluate_teacher(args)
    elif args.mode == 'schedule':
        pass


if __name__ == '__main__':
    main()
