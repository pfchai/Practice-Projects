#!/usr/bin/env python
# encoding: utf-8

import socket
import whois

ip = "pfchai.cn"

def get_whois_info(ip):
    """ 查询whois信息 """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('whois.internic.net', 43))   # 这里是用的互联网络信息中心的服务器，查询的域名信息有限
    s.send('sina.com.cn \r\n')

    info = ""
    while 1:
        v = s.recv(1024)
        if v == '' or v == None:
            break
        info += v
    s.close()

    return info

if __name__ == '__main__':
    print get_whois_info("sina.com.cn" + '\r\n')

    # 用的Python库，大部分域名都可以查到whois信息
    domainInfo = whois.whois(ip)
    print domainInfo
