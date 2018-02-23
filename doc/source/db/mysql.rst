mysql
===============

基本信息
--------

* 主机：localhost
* 端口：3306
* 用户：root
* 密码：root
* 数据库：test


表结构
-------

.. code-block:: sql

    -- ----------------------------
    -- Table structure for ebf_account
    -- ----------------------------
    DROP TABLE IF EXISTS `ebf_account`;
    CREATE TABLE `ebf_account` (
      `username` varchar(64) NOT NULL AUTO_INCREMENT COMMENT '账号',
      `password` varchar(256) NOT NULL COMMENT '密码',
      `nickname` varchar(64) DEFAULT NULL COMMENT '昵称',
      `user_type` int(1) DEFAULT 2 COMMENT '帐号类型',
      `upload_head` varchar(64) NOT NULL DEFAULT '1' COMMENT '头像',
      `now_type` int(1) DEFAULT 1 COMMENT '是否被禁用',
      PRIMARY KEY (`username`),
    ) ENGINE=ndbcluster AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COMMENT='用户表';

    -- ----------------------------
    -- Table structure for ebf_url
    -- ----------------------------
    DROP TABLE IF EXISTS `ebf_url`;
    CREATE TABLE `ebf_url` (
      `id` int(64) NOT NULL AUTO_INCREMENT COMMENT 'id',
      `url` varchar(256) NOT NULL COMMENT 'url地址',
      `icon` varchar(64) DEFAULT NULL COMMENT '菜单图标',
      `pid` int(1) NOT NULL DEFAULT '1' COMMENT '第几级菜单',
      `first` int(1) NOT NULL DEFAULT '1' COMMENT '否有二级菜单',
      PRIMARY KEY (`id`),
    ) ENGINE=ndbcluster AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COMMENT='菜单表';

    -- ----------------------------
    -- Table structure for ebf_role
    -- ----------------------------
    DROP TABLE IF EXISTS `ebf_role`;
    CREATE TABLE `ebf_role` (
      `id` int(64) NOT NULL AUTO_INCREMENT COMMENT 'id',
      `menu` varchar(256) NOT NULL COMMENT 'menu列表',
      PRIMARY KEY (`id`),
    ) ENGINE=ndbcluster AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COMMENT='角色拥有的菜单';

    -- ----------------------------
    -- Table structure for ebf_menu_role
    -- ----------------------------
    DROP TABLE IF EXISTS `ebf_menu_role`;
    CREATE TABLE `ebf_menu_role` (
      `id` int(64) NOT NULL AUTO_INCREMENT COMMENT 'id',
      `name` varchar(256) NOT NULL COMMENT '角色名',
      PRIMARY KEY (`id`),
    ) ENGINE=ndbcluster AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COMMENT='角色表';