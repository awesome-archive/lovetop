# -*- coding: utf-8 -*-

from spider import Spider
from threading import Thread


s = Spider()

#一刻钟采集一次
node_quarter_spider = {
    'zhihu':s.spider_zhihu,         #知乎热榜
    'tieba':s.spider_tieba,         #贴吧热榜
    'baidu':s.spider_baidu,         #百度实时热点
    'vsite':s.spider_vsite,         #V站排行榜
    'weibo':s.spider_weibo,         #微博
    'weixin':s.spider_weixin,       #微信
    'huxiu':s.spider_huxiu,         #虎嗅
    'ithome':s.spider_ithome,       #it之家
    'kr':s.spider_kr,               #36氪
    'cctvnews':s.spider_cctvnews,   #央视要闻
    'sspai':s.spider_sspai,         #少数派热文
    'ppnews':s.spider_ppnews,       #澎湃新闻
    }

#每天只需采集一次
node_day_spider = {
    'bsite':s.spider_bsite,         #B站
}

def spiders():
    return node_quarter_spider,node_day_spider


