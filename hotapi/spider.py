# -*- coding: utf-8 -*-

import json
import requests
from lxml import etree
from threading import Timer

huxiu_api = 'https://www.huxiu.com'
ithome_api ='https://www.ithome.com/'
ppnews_api = 'https://www.thepaper.cn/' #澎湃新闻
weixin_api = "https://weixin.sogou.com/"
baidu_api = "http://top.baidu.com/buzz?b=1"
vsite_api = "https://www.v2ex.com/?tab=hot"
kr_api = 'https://36kr.com/hot-list/catalog'
cctvnews_api = "http://news.cctv.com/data/index.json"
bsite_api = 'https://www.bilibili.com/ranking/all/0/0/3'
weibo_api = "https://s.weibo.com/top/summary?cate=realtimehot"
tieba_api = "http://tieba.baidu.com/hottopic/browse/topicList?res_type=1"
zhihu_api = 'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true'
sspai_api = 'https://sspai.com/api/v1/article/tag/page/get?limit=40&offset=0&tag=%E7%83%AD%E9%97%A8%E6%96%87%E7%AB%A0&released=false'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

#组装数据
def packdata(para_data):
    list_data = []
    for i in para_data:
        data = {}
        data["title"]=i[0]
        data["url"]=i[1]
        list_data.append(data)
    return list_data
    
class Spider(object):
    def __init__(self,url=None):
        if url!=None:
            self.url = url
            self.res = requests.get(url,headers=headers)
            self.res.encoding = "utf-8"
            self.soup = etree.HTML(self.res.text)

    #知乎热榜
    def spider_zhihu(self):
        list_zhihu = [] #此列表用于储存解析结果
        res = Spider(zhihu_api).res  
        #逐步解析接口返回的json
        zhihu_data = json.loads(res.text)['data']
        for part_zhihu_data in zhihu_data:              #遍历每一个data对象
            zhihu_id = "https://www.zhihu.com/question/"+str(part_zhihu_data['target']['id'])    #从对象得到问题的id
            zhihu_title = part_zhihu_data['target']['title'] #从对象得到问题的title
            list_zhihu.append([zhihu_title,zhihu_id])          #将id 和title组为一个列表，并添加在list_zhihu列表中
        return packdata(list_zhihu)
    
    #微博热搜
    def spider_weibo(self):
        list_weibo = [] #此列表用于储存解析结果
        weibo = "https://s.weibo.com"
        soup = Spider(weibo_api).soup
        for soup_a in soup.xpath("//td[@class='td-02']/a"):
            wb_title = soup_a.text
            wb_url = weibo + soup_a.get('href')
            if "javascript:void(0)" in wb_url: #过滤微博的广告，做个判断
                pass
            else:
                list_weibo.append([wb_title,wb_url])
        return packdata(list_weibo)

    #贴吧热度榜单
    def spider_tieba(self):
        list_tieba = []
        soup = soup = Spider(tieba_api).soup
        for soup_a in soup.xpath("//a[@class='topic-text']"):
            tieba_title = soup_a.text
            tieba_url = soup_a.get('href')
            list_tieba.append([tieba_title,tieba_url])
        return packdata(list_tieba)

    #V2EX热度榜单 20条
    def spider_vsite(self):
        list_v2ex = []
        vsite ="https://www.v2ex.com"
        soup = Spider(vsite_api).soup
        for soup_a in soup.xpath("//span[@class='item_title']/a"):
            vsite_title = soup_a.text
            vsite_url = vsite+soup_a.get('href')
            list_v2ex.append([vsite_title,vsite_url])
        return packdata(list_v2ex)

    #B站排行榜 100条
    def spider_bsite(self):
        list_bsite = []
        soup = Spider(bsite_api).soup
        for i in soup.xpath("//div[@class='info']/a"):
            bsite_title = i.xpath('text()')[0]
            bsite_url = i.get('href')
            list_bsite.append([bsite_title,bsite_url])
        return packdata(list_bsite)
    
    #百度实时热点 50条
    def spider_baidu(self):
        list_baidu = []
        res = Spider(baidu_api).res
        res.encoding='gb2312'
        soup = etree.HTML(res.text)
        for soup_a in soup.xpath("//a[@class='list-title']"):
            baidu_title = soup_a.text
            baidu_url = soup_a.get('href')
            list_baidu.append([baidu_title,baidu_url])
        return packdata(list_baidu)
    
    #微信热门文章 50条
    def spider_weixin(self):
        list_weixin = []
        soup = Spider(weixin_api).soup
        for soup_a in soup.xpath("//div[@class='txt-box']/h3/a"):
            weixin_title = soup_a.text
            weixin_url = soup_a.get('href')
            list_weixin.append([weixin_title,weixin_url])
        return packdata(list_weixin)

    #央视要闻
    def spider_cctvnews(self):
        list_cctvnews = []
        res = Spider(cctvnews_api).res
        json_cctv = json.loads(res.text)
        for i in json_cctv['rollData']:
            cctv_title = i['title']
            cctv_url = i['url']
            list_cctvnews.append([cctv_title,cctv_url])
        return packdata(list_cctvnews)

    #IT之家
    def spider_ithome(self):
        list_ithome = []
        soup = Spider(ithome_api).soup
        for soup_a in soup.xpath("//div/ul/li/a"):
            if soup_a.get('title') != None:
                ithome_title = soup_a.get('title')
                ithome_url = soup_a.get('href')
                list_ithome.append([ithome_title,ithome_url])
        return packdata(list_ithome)

    #36kr
    def spider_kr(slef):
        list_kr = []
        soup = Spider(kr_api).soup
        for soup_a in soup.xpath("//a[@class='article-item-title weight-bold']"):
            kr_title = soup_a.text
            kr_url = "https://36kr.com"+soup_a.get('href')
            list_kr.append([kr_title,kr_url])
        return packdata(list_kr)

    #虎嗅
    def spider_huxiu(slef):
        list_huxiu = []
        soup = Spider(huxiu_api).soup
        urls = soup.xpath("//div[@class='focus-item-right-wrap']/a/@href")
        titles = soup.xpath("//div[@class='focus-item-right-wrap']/a/div/p/text()")
        for i in range(0,len(urls)):
            huxiu_title = titles[i].strip().strip("\n").strip()
            huxiu_url = huxiu_api+urls[i]
            list_huxiu.append([huxiu_title,huxiu_url])
        return packdata(list_huxiu)
    
    #少数派热门
    def spider_sspai(self):
        list_sspai = []
        res = Spider(sspai_api).res
        for i in json.loads(res.text)['data']:
            sspai_title = i['title']
            sspai_url = 'https://sspai.com/post/'+str(i['id'])
            list_sspai.append([sspai_title, sspai_url])
        return packdata(list_sspai)

    #澎湃新闻
    def spider_ppnews(slef):
        list_ppnews = []
        soup = Spider(ppnews_api).soup
        for soup_a in soup.xpath("//ul[@class='list_hot']/li/a"):
            ppnews_title = soup_a.text
            ppnews_url = ppnews_api+soup_a.get('href')
            list_ppnews.append([ppnews_title,ppnews_url])
        return packdata(list_ppnews)
    
    
