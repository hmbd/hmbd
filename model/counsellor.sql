/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50627
Source Host           : localhost:3306
Source Database       : counsellor

Target Server Type    : MYSQL
Target Server Version : 50627
File Encoding         : 65001

Date: 2016-07-26 23:09:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_4458c4f25ec6dc8c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_2f62040b16f0d530_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_1b17844e36ea3b6f_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add user', '7', 'add_user');
INSERT INTO `auth_permission` VALUES ('20', 'Can change user', '7', 'change_user');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete user', '7', 'delete_user');
INSERT INTO `auth_permission` VALUES ('22', 'Can add url', '8', 'add_url');
INSERT INTO `auth_permission` VALUES ('23', 'Can change url', '8', 'change_url');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete url', '8', 'delete_url');
INSERT INTO `auth_permission` VALUES ('25', 'Can add menu role', '9', 'add_menurole');
INSERT INTO `auth_permission` VALUES ('26', 'Can change menu role', '9', 'change_menurole');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete menu role', '9', 'delete_menurole');
INSERT INTO `auth_permission` VALUES ('28', 'Can add role', '10', 'add_role');
INSERT INTO `auth_permission` VALUES ('29', 'Can change role', '10', 'change_role');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete role', '10', 'delete_role');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$15000$r928DVCJasha$fH8l9XCr5LUCjhtNYGEUD0SWhC3KeqBdEMstQjqoTIA=', '2016-07-24 04:13:32', '1', 'root', '', '', '1131909224@qq.com', '1', '1', '2016-07-24 04:13:32');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_5b1ae58276caf137_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_65478d238638318c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_547d965bd64e506d_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_5950b2a8e6246c92_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `djang_content_type_id_77a5d1da65641b38_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_2ea5fa35f6e2c573_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_68027e4670ac29af_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'log entry', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'permission', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'group', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('4', 'user', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'content type', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'session', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'user', 'app', 'user');
INSERT INTO `django_content_type` VALUES ('8', 'url', 'app', 'url');
INSERT INTO `django_content_type` VALUES ('9', 'menu role', 'app', 'menurole');
INSERT INTO `django_content_type` VALUES ('10', 'role', 'app', 'role');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2016-07-24 04:13:05');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2016-07-24 04:13:05');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2016-07-24 04:13:05');
INSERT INTO `django_migrations` VALUES ('4', 'sessions', '0001_initial', '2016-07-24 04:13:06');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('daizijhwlyfeo4zj4xkr3w08doc3sld6', 'NDhiYjIzODE4MmE1Y2ZkYTNjNWExOTYyMzI0YTVlNzUzMzk4NjI4ZTp7InVwbG9hZF9oZWFkIjoic3RhdGljL3VwbG9hZC9cdTUyMThcdTRlYTZcdTgzZjIuanBnIiwiX2RqYW5nb19jYXB0Y2hhX2tleSI6IiIsInVzZXJuYW1lIjoiYWRtaW4ifQ==', '2016-08-07 14:09:32');
INSERT INTO `django_session` VALUES ('g9xt8siethjukez0hoci2c0wptwttul0', 'NmQ2YmIxZjkyODMxMzAzMzNmMDVjM2Q3MzM1NGNmNTk5YTcwMGI0Zjp7InVwbG9hZF9oZWFkIjoic3RhdGljL3VwbG9hZC9cdTUyMThcdTRlYTZcdTgzZjIuanBnIiwiX2RqYW5nb19jYXB0Y2hhX2tleSI6Ijdlc1IiLCJ1c2VybmFtZSI6ImFkbWluIn0=', '2016-08-09 15:01:40');
INSERT INTO `django_session` VALUES ('so1y83nwz67142m9a4v4tyqat3ebhlot', 'YWZhNTllYjI5OGRlZmYyNThiZTE2OGEzMzUyOWNjMDgwNmE2NzFmNDp7InVwbG9hZF9oZWFkIjoic3RhdGljL3VwbG9hZC9cdTUyMThcdTRlYTZcdTgzZjIuanBnIiwidXNlcm5hbWUiOiJhZG1pbiIsIl9kamFuZ29fY2FwdGNoYV9rZXkiOiIifQ==', '2016-08-07 15:39:16');
INSERT INTO `django_session` VALUES ('tuku068d8pofkqtpod00el42ulmyaz0x', 'NDhiYjIzODE4MmE1Y2ZkYTNjNWExOTYyMzI0YTVlNzUzMzk4NjI4ZTp7InVwbG9hZF9oZWFkIjoic3RhdGljL3VwbG9hZC9cdTUyMThcdTRlYTZcdTgzZjIuanBnIiwiX2RqYW5nb19jYXB0Y2hhX2tleSI6IiIsInVzZXJuYW1lIjoiYWRtaW4ifQ==', '2016-08-07 10:34:11');
INSERT INTO `django_session` VALUES ('u8csm0dp99769e3i73wmfvomss333wex', 'ZTEyY2M5NTgwMzU5Y2MzNTU5YjAyYTIzNjBkMzUyMmQ1ZTFmZjE0ZTp7InVwbG9hZF9oZWFkIjoic3RhdGljL3VwbG9hZC9cdTUyMThcdTRlYTZcdTgzZjIuanBnIiwiX2RqYW5nb19jYXB0Y2hhX2tleSI6IlVRTlMiLCJ1c2VybmFtZSI6ImFkbWluIn0=', '2016-08-07 10:35:36');
INSERT INTO `django_session` VALUES ('vm4wsq7i3fbj869w0ebpeho9uha7sfcb', 'MjFlNDkwMzdkOTRkODBkNWQ4ZTZkYzg5Mzc4OGRlNzE1NzRhODMwYTp7InVzZXJuYW1lIjoiYWRtaW4iLCJ1cGxvYWRfaGVhZCI6InN0YXRpYy91cGxvYWQvXHU1MjE4XHU0ZWE2XHU4M2YyLmpwZyIsIl9kamFuZ29fY2FwdGNoYV9rZXkiOiIifQ==', '2016-08-07 14:13:29');

-- ----------------------------
-- Table structure for ebf_account
-- ----------------------------
DROP TABLE IF EXISTS `ebf_account`;
CREATE TABLE `ebf_account` (
  `username` varchar(64) NOT NULL,
  `password` varchar(256) NOT NULL,
  `nickname` varchar(64) NOT NULL,
  `user_type` int(64) NOT NULL,
  `upload_head` varchar(64) NOT NULL,
  `now_type` varchar(64) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ebf_account
-- ----------------------------
INSERT INTO `ebf_account` VALUES ('1', 'pbkdf2_sha256$15000$A$x4MHTRAYMWGTtyR6HtqDgOgtPnFNwGWz3nT4VBirtKs=', '1', '2', 'static/img/upload/xingguo.jpg', '1');
INSERT INTO `ebf_account` VALUES ('2', 'pbkdf2_sha256$15000$A$CXnuT6VE0QSQycvFkubw08Z6M1S+6FRXc6hj56PUayk=', '2', '2', 'static/img/upload/xingguo.jpg', '1');
INSERT INTO `ebf_account` VALUES ('3', 'pbkdf2_sha256$15000$A$Z3XnKqhS4SUE+O6y6WB9ZMH8Ikh3GNZFCEhegjtTk3M=', '3', '3', 'static/img/upload/webwxgeticon.jpg', '1');
INSERT INTO `ebf_account` VALUES ('4', 'pbkdf2_sha256$15000$A$Vu+HO/Rm6WEoW6jr1A0MGcDfJcnHdOYzr1Obpzf6dAw=', '4', '4', 'static/img/upload/git.png', '1');
INSERT INTO `ebf_account` VALUES ('admin', 'pbkdf2_sha256$12000$A$tYnrI1fHx175ufLALASydwN3wUirAL2SvwwrDntxDyU=', 'admin', '1', 'static/img/upload/刘亦菲.jpg', '1');

-- ----------------------------
-- Table structure for ebf_menu_role
-- ----------------------------
DROP TABLE IF EXISTS `ebf_menu_role`;
CREATE TABLE `ebf_menu_role` (
  `id` int(64) NOT NULL,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ebf_menu_role
-- ----------------------------
INSERT INTO `ebf_menu_role` VALUES ('2', '普通用户');
INSERT INTO `ebf_menu_role` VALUES ('3', '会员');
INSERT INTO `ebf_menu_role` VALUES ('4', '超级会员');

-- ----------------------------
-- Table structure for ebf_role
-- ----------------------------
DROP TABLE IF EXISTS `ebf_role`;
CREATE TABLE `ebf_role` (
  `id` int(64) NOT NULL,
  `menu` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ebf_role
-- ----------------------------
INSERT INTO `ebf_role` VALUES ('2', '1,2,21');
INSERT INTO `ebf_role` VALUES ('3', '1,2,21,22,23');
INSERT INTO `ebf_role` VALUES ('4', '1,2,21,22,23,4');

-- ----------------------------
-- Table structure for ebf_url
-- ----------------------------
DROP TABLE IF EXISTS `ebf_url`;
CREATE TABLE `ebf_url` (
  `id` int(64) NOT NULL,
  `url` varchar(64) DEFAULT NULL,
  `name` varchar(64) NOT NULL,
  `icon` varchar(64) DEFAULT NULL,
  `pid` int(64) NOT NULL,
  `first` int(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ebf_url
-- ----------------------------
INSERT INTO `ebf_url` VALUES ('1', 'main', '首页', '', '0', '2');
INSERT INTO `ebf_url` VALUES ('2', '', '菜单', null, '0', '1');
INSERT INTO `ebf_url` VALUES ('3', 'statistics', 'QQ在线人数', null, '0', '2');
INSERT INTO `ebf_url` VALUES ('4', 'ad_content', '表格显示', null, '0', '2');
INSERT INTO `ebf_url` VALUES ('5', 'menu', '角色菜单', null, '0', '2');
INSERT INTO `ebf_url` VALUES ('21', 'mongodb_add', '添加信息', null, '2', '0');
INSERT INTO `ebf_url` VALUES ('22', 'mongodb_query', '查询信息', null, '2', '0');
INSERT INTO `ebf_url` VALUES ('23', 'weight_run', '折线图', null, '2', '0');
