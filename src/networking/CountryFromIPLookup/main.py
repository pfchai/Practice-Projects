#!/usr/bin/env python
# encoding: utf-8

"IP地址是直接使用的ipip.net提供的api"

import requests

def get_ip_info(ip):
    req = requests.get("http://freeapi.ipip.net/" + ip)
    return req.content


if __name__ == '__main__':
    print get_ip_info("115.28.7.105")
