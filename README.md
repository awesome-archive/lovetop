# lovetop
吾爱热榜开源代码

#### 「极简效率」工具

演示地址： https://lovetop.top/

#### 说明
##### 后端部分：使用FastApi框架 配合uvicorn 完成

依赖的外部库
`pip install lxml`

`pip install reuqests` 

一个基于 asyncio 开发的一个轻量级高效的 Web 服务器框架

`pip install uvicorn`  

`pip install fastapi` 

国内推荐添加清华源 参数  `-i https://pypi.tuna.tsinghua.edu.cn/simple` 以加快安装速度


##### 前端部分：主要使用了Layui框架渲，使用JavaScript+html+css 构造前端

#### 文件结构

后端部分

├─hotapi  存放后端python代码  
│  webapi.py  
│  spider.py  
│  scheduler.py  
│  index.html 主页文件  
│  
├─ext  扩展  
│  ├─css  
│  │      style.css 卡片控制的相关css  
│  │      webkit.css  滚动条央视  
│  ├─img  存放图片 各网站logo  
│  ├─js  
│  │      index.js  主页渲染  
│  │      render.js 渲染函数 导航监听  
│  └─page  
└─layui layui框架  
