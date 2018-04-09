# 简介  
> django后台系统

## 依赖的插件
* mysql
* mongodb
* redis

## 注意
* app/\__init__.py中千万不要引入model和同级的urls,views
* Python版本3.4.1, Django版本1.7,注意两者的版本兼容
* mysql启动方式不能用socket启动
* Pillow
    > 安装前先安装python lib
    ```
    sudo apt-get install libjpeg8-dev
    sudo apt-get install libfreetype6-dev
    sudo apt-get install python-imaging
    ```

## kill掉django进程
> ps axu| grep manage.py | grep -v grep | awk '{print $2}' | xargs kill -9

## 其他详细内容在查看帮助文档
 * doc-->build-->html-->index.html   

[![内容任意](https://github.com/1131909224/hmbd/blob/master/static/img/upload/xingguo.jpg "点击图片进入我的博客")](https://hmbd.github.io)

[博客地址](https://hmbd.github.io)
