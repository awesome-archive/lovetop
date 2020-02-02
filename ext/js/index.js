/*用get到的数据来渲染前端*/

var site_list=new Array("zhihu","vsite","weibo",
"tieba","baidu","weixin","kr","huxiu","ithome",
"cctvnews","ppnews","sspai");
//元素名字，同时也是参数后name的值,limit_num 也即每次请求多少条数据

//开始渲染
for (i = 0; i < site_list.length; i++) { 
    render(site_list[i],15);
}