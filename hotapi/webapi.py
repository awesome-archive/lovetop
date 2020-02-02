# -*- coding: utf-8 -*-

import time
import math
from spider import Spider
from threading import Timer
from threading import Thread
from scheduler import spiders
from fastapi import FastAPI,Header
from starlette.middleware.cors import CORSMiddleware

#fastapi实例化
app = FastAPI()

#设置可获取接口数据的地址
origins = ["http://127.0.0.1","https://lovetop.top",]
#设置跨域传参
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#初始化全局变量，存放各网站数据
node_data = {}

#设置spiders()对象
quarter_spiders = spiders()[0] #一刻钟爬虫列表
day_spiders = spiders()[1]  #日更爬虫列表

class Manage(object):

    def __init__(self):
        pass
    
    def time_derive(self, name, spider_list):
        global node_data
        if spider_list[name]() != []:  #加一个判断，如果请求数据为空，则不再更新数据
            node_data[name] = spider_list[name]()

    def time_task(self, min, spider_list):
        for node_name in spider_list.keys():
            Thread(target=self.time_derive,args=(node_name,spider_list,)).start() #将每个节点加入线程之中
            time.sleep(0.1) #延时0.1秒，防止线程过多出错
        Timer(min*60,self.time_task,(min, spider_list,)).start()  #定时

Manage().time_task(15,quarter_spiders)  #十五分钟更新一次
Manage().time_task(24*60,day_spiders)   #每天更新一次

#结果返回为layui标准json
"""
    limit : 设置每页data的条数
    page : 也即页数
    pages : 总页面数，取决于数据总条数、limit
"""

def handle_data(tdata, page, limit):
    part_data = tdata[page*limit-limit:page*limit]
    res = {}
    if tdata != []:
        res['code'] = 0
        res['msg'] = "Success"
        res['pages'] = int(math.ceil(len(tdata)/limit))
        res['count'] = len(part_data)
        res['data'] = part_data
    else:
        res['code'] = -1
        res['msg'] = "Fail"
        res['pages'] = 0
        res['count'] = 0
        res['data'] = 0       
    return res

#数据返回 默认 limit=15
def ret(name, page, limit):
    return handle_data(node_data[name],page, limit)

#首页
@app.get("/")
def read_items(*, user_agent: str = Header(None)):
    return {"User-Agent": user_agent}

#热点接口页面
@app.get("/hot")
def read_name(name: str, page: int,limit: int):
    return ret(name, page, limit)
