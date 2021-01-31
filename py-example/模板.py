import requests  # 导入网络模块
import os  # 导入文件模块
import re  # 导入正则模块
import json  # json模块
from selenium import webdriver  # 导入自动化模块
from lxml import etree  # 导入xpath模块

if __name__ == '__main__':
    url = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers).text

    tree = etree.HTML(response)
    li_lsit = tree.xpath("")

    # if not os.path.exists('./'):
    #     os.mkdir('./')
    # fp = open('./','w')


