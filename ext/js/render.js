
layui.use('element', function(){
  var element = layui.element; //导航的hover效果、二级菜单等功能，需要依赖element模块
  //监听导航点击
  element.on('nav(demo)', function(elem){
    //console.log(elem)
    layer.msg(elem.text());
  });
});

/*接口地址*/
var api_hot = "http://127.0.0.1:8080/hot";

function render(elem_name, limit_num){
  layui.use('flow', function(){
    var $ = layui.jquery; //不用额外加载jQuery，flow模块本身是有依赖jQuery的，直接用即可。
    var flow = layui.flow;
    flow.load({
      elem: "#"+elem_name //指定列表容器
      ,end: "没有更多了"
      ,scrollElem: "#"+elem_name+"card" //滚动条元素
      ,mb:30
      ,done: function(page, next){ //到达临界点（默认滚动触发），触发下一页
        var lis = [];
        //以jQuery的Ajax请求为例，请求下一页数据（注意：page是从2开始返回）
        $.get(api_hot+"?name="+elem_name+"&page="+page+"&limit="+limit_num, function(res){
          //假设你的列表返回在data集合中
          layui.each(res.data, function(index, item){
            var num = index+1;
            var num2 = page-1;
            var num3 = num+num2*15;
            /*
            <li>
              <a target='_blank' href='http://www.baidu.com'>
                <img src='./ext/img/no1.png' width='35' height='20'>
                ceshi
              </a>
            </li>
            */
            if(num3<=3){
              var img_1 = "<img src='./ext/img/no1.png' width='32' height='18'>"
              var img_2 = "<img src='./ext/img/no2.png' width='32' height='18'>"
              var img_3 = "<img src='./ext/img/no3.png' width='32' height='18'>"
              var str_left = '<li>'+"<a target='_blank' href='"+item.url+"'>";
              var str_right = "    "+item.title+'</a></li>';
              switch(num3){
                case 1:
                  lis.push(str_left+img_1+str_right);
                  break;
                case 2:
                  lis.push(str_left+img_2+str_right);
                  break;
                case 3:
                  lis.push(str_left+img_3+str_right);
                  break;
            }
           }else{
            var strnum = "<font color='#009688'>"+num3+"      "+"</font>";

            var str_all = '<li>'+"<a target='_blank' href='"+item.url+"'"+strnum+item.title+'</a></li>';
            lis.push(str_all);
           }
          }); 
          //执行下一页渲染，第二参数为：满足“加载更多”的条件，即后面仍有分页
          //pages为Ajax返回的总页数，只有当前页小于总页数的情况下，才会继续出现加载更多
          next(lis.join(''), page < res.pages);    
        });
      }
    });
  });
}
