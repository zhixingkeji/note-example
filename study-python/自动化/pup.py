import requests  # 导入网络模块
import os  # 导入文件模块
import re  # 导入正则模块
import json  # json模块
from time import sleep  # 时间模块
import random # 随机模块
from selenium import webdriver  # 导入自动化模块
from lxml import etree  # 导入xpath模块
from you_get import common
from multiprocessing.dummy import Pool


def get_page():
    # 第一页的地址
    first_url = 'https://www.bilibili.com/video/BV1ot411y7mU?p=1'

    # 浏览器ID
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }

    # 获取页面数据
    response = requests.get(url=first_url, headers=headers).text

    # 获取xpath对象
    tree = etree.HTML(response)

    # 使用xpath进行解析到一个列表
    li_lsit = tree.xpath('//*[@id="multi_page"]/div[2]/ul/li')

    # 列表里有多少个元素代表了有多少P
    page = len(li_lsit)

    # 返回p数
    return page


if __name__ == '__main__':
    page = get_page()
    for p in range(1, page + 1):
        down_url = 'https://www.bilibili.com/video/BV1ot411y7mU?p=' + str(p)
        print("\n\n现在下的是第"+str(p)+'个视频....\n\n')
        downdir = r'F:\下载'
        common.any_download(url=down_url, stream_id='flv', info_only=False, output_dir=downdir, merge=True)
        print("\n\n第" + str(p) + '个视频下载成功!!!\n\n')