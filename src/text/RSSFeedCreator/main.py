#!/usr/bin/env python
# encoding: utf-8

from feedgen.feed import FeedGenerator
from csdn import CSDN

def make_csdn_rss():
    fg = FeedGenerator()
    fg.id('http://blog.csdn.net')
    fg.title(u'CSDN 博客频道')
    fg.author({'name': 'pfchai',})
    fg.link(href='http://blog.csdn.net', rel='self')
    fg.description(u"csdn 首页博客")

    csdn = CSDN()
    for item in csdn.get_item():
        fe = fg.add_entry()
        fe.id(item['link'])
        fe.title(item['title'])
        fe.author({'name': item['author']})
        fe.description(item['description'])
        fe.content(item['description'])

    return fg

if __name__ == '__main__':
    fg = make_csdn_rss()
    #  fg.rss_str('csdn_rss.xml')
    #  fg.atom_file('csdn_atom.xml')
    rssFeed = fg.rss_str(pretty=True)
    atomFeed = fg.atom_str(pretty=True)
    print rssFeed
    print atomFeed

