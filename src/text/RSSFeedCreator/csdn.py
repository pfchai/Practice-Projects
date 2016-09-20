#!/usr/bin/env python
# encoding: utf-8

import requests
from bs4 import BeautifulSoup

class CSDN(object):
    """ 抓取CSDN博客首页的文章"""
    def __init__(self):
        self.headers = {
            'Host': 'blog.csdn.net',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': 1,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.csdn.net/',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',}
        self.url = "http://blog.csdn.net"

    def _download_html(self):
        """ 下载首页html页面 """
        response = requests.get(self.url, headers=self.headers)
        return response.content

    def get_item(self):
        """ 返回文章条目 """

        soup = BeautifulSoup(self._download_html())
        for blog in soup.find_all("dl", class_="blog_list"):
            author = blog.dt.a.next_sibling.next_sibling.text
            title = blog.dd.h3.text
            description = blog.div.text
            link = blog.dd.h3.a['href']
            yield {'title': title, 'author': author, 'link': link, 'description': description}


if __name__ == '__main__':
    csdn = CSDN()
    for i in csdn.get_item():
        print i['title']
