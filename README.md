# lovetop
吾爱热榜开源代码  技术讨论QQ群 8805926

### 「极简效率」工具

演示地址： https://lovetop.top/

### 1.说明：
#### 后端部分：使用FastApi框架 配合uvicorn 完成
#### 前端部分：主要使用了Layui框架渲，使用JavaScript+html+css 构造前端
依赖的外部库：    
`pip install lxml`  
`pip install reuqests`   
`pip install uvicorn`(一个基于 asyncio 开发的一个轻量级高效的 Web 服务器框架)  
`pip install fastapi`   
国内推荐添加清华源 参数  `-i https://pypi.tuna.tsinghua.edu.cn/simple` 以加快安装速度  

### 2.文件结构

主要文件说明：  
`webapi.py `    fastapi Web页面  
`spider.py`     抓取器  
`scheduler.py`  调度器  
`index.html`    主页文件  
`/ext/css/style.css` 卡片控制的相关css  
`/ext/css/webkit.css` 滚动条控制   
`/ext/img`  存放图片 各网站logo   
`/ext/js/index.js`  主页渲染    
`/ext/js/render.js` 渲染函数 导航监听    

### 3.请求格式与数据返回：  
请求示例： https://lovetop.top:8080/hot?name=zhihu&page=1&limit=10  

参数说明：  
1.`name`要请求的节点名  
2.`page`第几页
3.`limit`每页的数量

返回格式：  
![avatar](https://raw.githubusercontent.com/LookCos/lovetop/master/preview/json.jpg)
### 4.如何运行：
执行：  
`uvicorn main:app --host 0.0.0.0 --port 80 --reload`  
参数说明 `main`是文件名，`--reload`是开发者模式，相当于Flask中`debug=True`  

### 参考文档：  
[1] Layui官方文档       https://www.layui.com/doc/  
[2] 清华pip源 使用说明 https://mirrors.tuna.tsinghua.edu.cn/help/pypi/  
[3]  FastApi文档       https://fastapi.tiangolo.com/deployment/  
[4]  Uvicorn文档       https://www.uvicorn.org/deployment
