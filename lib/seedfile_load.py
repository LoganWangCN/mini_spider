#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File: seedfile_load.py
@Author:  logan
@Time:    2017-08-03
@Description:
1. 读取种子文件
2. 去除行尾的换行符，去重
"""


def seedfile_load(file_path):
    with open(file_path, 'r') as f:
        urls = list(set(line.strip('\n') for line in f))
        return urls


if __name__ == '__main__':
    urls = seedfile_load('../urls')
    print urls
