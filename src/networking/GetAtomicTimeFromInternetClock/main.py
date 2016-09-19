#!/usr/bin/env python
# encoding: utf-8

import socket
import struct
import time

timeServer = "time.7x24s.com"
port = 123

def get_time():
    TIME_1970 = 2208988800L
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'
    client.sendto(data, (timeServer, port))
    data, address = client.recvfrom(1024)
    data_result = struct.unpack('!12I', data)[10]
    data_result -= TIME_1970
    return data_result


if __name__ == '__main__':
    print time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(get_time()))
