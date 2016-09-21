#!/usr/bin/env python
# encoding: utf-8

import requests
from bs4 import BeautifulSoup
import re

headers = {
    'Host': 'alexa.ip138.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://alexa.ip138.com/post/search.asp',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',}

def get_info(html):
    soup = BeautifulSoup(html)
    tables = soup.find_all('table')
    table = tables[3]
    rows = table.find_all("tr")
    info = []
    for row in rows[1:-1]:
        cells = row.find_all("td")
        info.append([cells[0].text, cells[1].text])

    t = table.find('a')['href'].split("=")[-1]
    pageTotal = re.findall(r"\d+", rows[-1].text)[2]
    return [info, pageTotal, t]

def get_html(zipCode):
    payload = {"zip": zipCode}
    r = requests.post("http://alexa.ip138.com/post/search.asp", headers=headers, data=payload)
    get_info(r.content)
    return r.content

def get_next_page(pageNum, t):
    url = "http://alexa.ip138.com/post/search.asp?page=" + pageNum + "&regionid=&cityid=&countyid=&address=&zip=214122&t=" + t
    res = requests.get(url)
    return res.content

def get_zip(zipCode):
    infos = []
    html = get_html(zipCode)
    [info, pageTotal, t] = get_info(html)
    infos += info
    for i in range(1, int(pageTotal)):
        html = get_next_page(str(i), t)
        info = get_info(html)[0]
        infos += info

    return infos


if __name__ == '__main__':
    infos = get_zip("214122")
    for i in infos:
        print i[0].encode('utf-8')
