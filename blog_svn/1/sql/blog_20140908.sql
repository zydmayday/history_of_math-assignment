/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50614
Source Host           : 127.0.0.1:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50614
File Encoding         : 65001

Date: 2014-09-09 00:22:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `article_article`
-- ----------------------------
DROP TABLE IF EXISTS `article_article`;
CREATE TABLE `article_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `post_time` datetime NOT NULL,
  `raw_content` varchar(9999) NOT NULL,
  `markdown_content` varchar(9999) NOT NULL,
  `abstract` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article_article
-- ----------------------------
INSERT INTO `article_article` VALUES ('17', '第一篇博客，中秋快乐', '2014-09-08 16:21:50', '\n这是我的第一篇博客，也不知道从什么说起，就说说我搭建这个博客的过程吧。\n\n###历史背景\n\n其实之前就一直有写博客的想法，不过当时正好在学**[Node.js][1]**，苦于Node.js的服务器不太好找（主要是我比较懒），所以就一直搁置了，我自己还跟着网上的人学做了一个基于Node.js的简易版的blog。后来跟着[吴磊][2]大神的步伐，就自己试着做了一个blog出来，目前还很简陋，不过功能会一步步完善了，只要迈出了第一步，之后的就好说了。\n\n----------\n\n###博客搭建\n这次我学乖了，用了屌炸天的**[Django][3]**作为开发语言，我的实践证明这个语言还是很靠谱，很高效的，如果不是因为我卡在**[SAE][4]**上的环境搭建的话，我估计任何人上手之后一天时间就可以搭建一个简单的不能再简单的博客出来。\n截止现在，我只是做了最基本的功能，博客的显示和标签功能。虽然界面什么的是丑了点，不过起码东西是可以放上去，也能看了，日后应该是会不断的对界面和功能进行加强和改进的。\n\n----------\n\n###项目用到的技术\n  我是看到Django中的[这段文档][5]然后决定写一个博客网站的。主要就是说针对ManyToManyField的一个补充，虽然我现在说不上这个功能和普通的ManyToManyField有什么本质的区别，或者说这样使用对于我的模型搭建究竟有没有益处尚未可知，甚至有可能是多此一举，不过这也算是一次尝试。\n不过经过我的阅读我还是发现了一些优点的，比如：\n\n```\n>>> # Beatles have broken up\n>>> beatles.members.clear()\n>>> # Note that this deletes the intermediate model instances\n>>> Membership.objects.all()\n[]\n```\n像这样就可以很方便的解除模型之间的关联。\n\n 此外，我还用到了[Manager] [6]，用来强化创建的model模型，为其提供一些自带的方法，相当于Java中的创建对象，调用对象函数这样，感觉如果照这个思路写起来，代码的复用率会比较高，保持DRY很重要。 \n具体思路如下：\n```\n# 标签控制类\nclass LabelManager(models.Manager):\n	def render_labels(self):\n		labels = self.filter(number_is_used__gt=0).order_by(\'-number_is_used\').aggregate(Avg(\'number_is_used\'))[\'number_is_used__avg\'][:10]\n		return labels\n\n# 标签\nclass Label(models.Model):\n	name = models.CharField(max_length=25)\n	number_is_used = models.IntegerField()\n	objects = LabelManager()\n	def __unicode__(self):\n		return self.name\n```\n用一个Manager类来专门控制其对应model的动作，相当于原始model做结构控制，Manager做动作控制，这样理解的话，写起代码来也挺顺手。\n\n----------\n\n###总结\n突然发现用[markdown][7]写博客好累啊。。写了我好久\n总之这也算是我的一个新的开始了，接下来还有很多工作需要做，需要去完善，中秋快乐~\n\n  [1]: http://nodejs.org/\n  [2]: http://fredsneverland.com/\n  [3]: https://www.djangoproject.com/\n  [4]: http://sae.sina.com.cn/\n  [5]: https://docs.djangoproject.com/en/1.7/topics/db/models/#extra-fields-on-many-to-many-relationships\n  [6]: https://docs.djangoproject.com/en/1.7/topics/db/managers/#custom-managers\n  [7]: http://en.wikipedia.org/wiki/Markdown\n\n', '<p>这是我的第一篇博客，也不知道从什么说起，就说说我搭建这个博客的过程吧。</p>\n\n\n\n<h3 id=\"历史背景\">历史背景</h3>\n\n<p>其实之前就一直有写博客的想法，不过当时正好在学<strong><a href=\"http://nodejs.org/\">Node.js</a></strong>，苦于Node.js的服务器不太好找（主要是我比较懒），所以就一直搁置了，我自己还跟着网上的人学做了一个基于Node.js的简易版的blog。后来跟着<a href=\"http://fredsneverland.com/\">吴磊</a>大神的步伐，就自己试着做了一个blog出来，目前还很简陋，不过功能会一步步完善了，只要迈出了第一步，之后的就好说了。</p>\n\n<hr>\n\n\n\n<h3 id=\"博客搭建\">博客搭建</h3>\n\n<p>这次我学乖了，用了屌炸天的<strong><a href=\"https://www.djangoproject.com/\">Django</a></strong>作为开发语言，我的实践证明这个语言还是很靠谱，很高效的，如果不是因为我卡在<strong><a href=\"http://sae.sina.com.cn/\">SAE</a></strong>上的环境搭建的话，我估计任何人上手之后一天时间就可以搭建一个简单的不能再简单的博客出来。 <br>\n截止现在，我只是做了最基本的功能，博客的显示和标签功能。虽然界面什么的是丑了点，不过起码东西是可以放上去，也能看了，日后应该是会不断的对界面和功能进行加强和改进的。</p>\n\n<hr>\n\n\n\n<h3 id=\"项目用到的技术\">项目用到的技术</h3>\n\n<p>我是看到Django中的<a href=\"https://docs.djangoproject.com/en/1.7/topics/db/models/#extra-fields-on-many-to-many-relationships\">这段文档</a>然后决定写一个博客网站的。主要就是说针对ManyToManyField的一个补充，虽然我现在说不上这个功能和普通的ManyToManyField有什么本质的区别，或者说这样使用对于我的模型搭建究竟有没有益处尚未可知，甚至有可能是多此一举，不过这也算是一次尝试。 <br>\n不过经过我的阅读我还是发现了一些优点的，比如：</p>\n\n\n\n<pre class=\"prettyprint\"><code class=\" hljs python\"><span class=\"hljs-prompt\">&gt;&gt;&gt; </span><span class=\"hljs-comment\"># Beatles have broken up</span>\n<span class=\"hljs-prompt\">&gt;&gt;&gt; </span>beatles.members.clear()\n<span class=\"hljs-prompt\">&gt;&gt;&gt; </span><span class=\"hljs-comment\"># Note that this deletes the intermediate model instances</span>\n<span class=\"hljs-prompt\">&gt;&gt;&gt; </span>Membership.objects.all()\n[]</code></pre>\n\n<p>像这样就可以很方便的解除模型之间的关联。</p>\n\n<p>此外，我还用到了<a href=\"https://docs.djangoproject.com/en/1.7/topics/db/managers/#custom-managers\">Manager</a>，用来强化创建的model模型，为其提供一些自带的方法，相当于Java中的创建对象，调用对象函数这样，感觉如果照这个思路写起来，代码的复用率会比较高，保持DRY很重要。  <br>\n具体思路如下：</p>\n\n\n\n<pre class=\"prettyprint\"><code class=\" hljs python\"><span class=\"hljs-comment\"># 标签控制类</span>\n<span class=\"hljs-class\"><span class=\"hljs-keyword\">class</span> <span class=\"hljs-title\">LabelManager</span><span class=\"hljs-params\">(models.Manager)</span>:</span>\n    <span class=\"hljs-function\"><span class=\"hljs-keyword\">def</span> <span class=\"hljs-title\">render_labels</span><span class=\"hljs-params\">(self)</span>:</span>\n        labels = self.filter(number_is_used__gt=<span class=\"hljs-number\">0</span>).order_by(<span class=\"hljs-string\">\'-number_is_used\'</span>).aggregate(Avg(<span class=\"hljs-string\">\'number_is_used\'</span>))[<span class=\"hljs-string\">\'number_is_used__avg\'</span>][:<span class=\"hljs-number\">10</span>]\n        <span class=\"hljs-keyword\">return</span> labels\n\n<span class=\"hljs-comment\"># 标签</span>\n<span class=\"hljs-class\"><span class=\"hljs-keyword\">class</span> <span class=\"hljs-title\">Label</span><span class=\"hljs-params\">(models.Model)</span>:</span>\n    name = models.CharField(max_length=<span class=\"hljs-number\">25</span>)\n    number_is_used = models.IntegerField()\n    objects = LabelManager()\n    <span class=\"hljs-function\"><span class=\"hljs-keyword\">def</span> <span class=\"hljs-title\">__unicode__</span><span class=\"hljs-params\">(self)</span>:</span>\n        <span class=\"hljs-keyword\">return</span> self.name</code></pre>\n\n<p>用一个Manager类来专门控制其对应model的动作，相当于原始model做结构控制，Manager做动作控制，这样理解的话，写起代码来也挺顺手。</p>\n\n<hr>\n\n\n\n<h3 id=\"总结\">总结</h3>\n\n<p>突然发现用<a href=\"http://en.wikipedia.org/wiki/Markdown\">markdown</a>写博客好累啊。。写了我好久 <br>\n总之这也算是我的一个新的开始了，接下来还有很多工作需要做，需要去完善，中秋快乐~</p>', '\n\n这是我的第一篇博客，也不知道从什么说起，就说说我搭建这个博客的过程吧。\n历史背景\n\n其实之前就一直有写博客的想法，不过当时正好在学Node.js，苦于Node.js的服务器不太好找（主要是我比较懒），所以就一直搁置了，我自己还跟着网上的人学做了一个基于Node.js的简易版的blog。后来跟着吴磊大神的步伐，就自己试着做了一个blog出来，目前还很简陋，不过功能会一步步完善了，只要迈出了第一步，之后的就好说了。');

-- ----------------------------
-- Table structure for `article_label`
-- ----------------------------
DROP TABLE IF EXISTS `article_label`;
CREATE TABLE `article_label` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `number_is_used` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article_label
-- ----------------------------
INSERT INTO `article_label` VALUES ('15', 'Django', '1');
INSERT INTO `article_label` VALUES ('16', '编程', '1');

-- ----------------------------
-- Table structure for `article_labelsinarticle`
-- ----------------------------
DROP TABLE IF EXISTS `article_labelsinarticle`;
CREATE TABLE `article_labelsinarticle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `label_id` int(11) NOT NULL,
  `date_joined` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `article_labelsinarticle_e669cc35` (`article_id`),
  KEY `article_labelsinarticle_e05256b6` (`label_id`),
  CONSTRAINT `article_id_refs_id_eee07f54` FOREIGN KEY (`article_id`) REFERENCES `article_article` (`id`),
  CONSTRAINT `label_id_refs_id_bcc12d15` FOREIGN KEY (`label_id`) REFERENCES `article_label` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article_labelsinarticle
-- ----------------------------
INSERT INTO `article_labelsinarticle` VALUES ('33', '17', '15', '2014-09-09');
INSERT INTO `article_labelsinarticle` VALUES ('34', '17', '16', '2014-09-09');

-- ----------------------------
-- Table structure for `auth_group`
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
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
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
INSERT INTO `auth_permission` VALUES ('19', 'Can add migration history', '7', 'add_migrationhistory');
INSERT INTO `auth_permission` VALUES ('20', 'Can change migration history', '7', 'change_migrationhistory');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete migration history', '7', 'delete_migrationhistory');
INSERT INTO `auth_permission` VALUES ('22', 'Can add label', '8', 'add_label');
INSERT INTO `auth_permission` VALUES ('23', 'Can change label', '8', 'change_label');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete label', '8', 'delete_label');
INSERT INTO `auth_permission` VALUES ('25', 'Can add article', '9', 'add_article');
INSERT INTO `auth_permission` VALUES ('26', 'Can change article', '9', 'change_article');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete article', '9', 'delete_article');
INSERT INTO `auth_permission` VALUES ('28', 'Can add labels in article', '10', 'add_labelsinarticle');
INSERT INTO `auth_permission` VALUES ('29', 'Can change labels in article', '10', 'change_labelsinarticle');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete labels in article', '10', 'delete_labelsinarticle');

-- ----------------------------
-- Table structure for `auth_user`
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
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$12000$V0qX9BrldUho$meDWHAyn8+GjV/FIQ6IaSYYiDLAP6SlyZV+8mq8u780=', '2014-09-07 09:21:25', '1', 'zyd', '', '', 'zydmayday@sina.com', '1', '1', '2014-09-07 09:03:21');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2014-09-07 09:21:33', '1', '9', '1', 'Article object', '1', '');
INSERT INTO `django_admin_log` VALUES ('2', '2014-09-07 09:23:53', '1', '8', '1', 'Label object', '1', '');
INSERT INTO `django_admin_log` VALUES ('3', '2014-09-08 07:36:33', '1', '8', '4', 'Label object', '3', '');
INSERT INTO `django_admin_log` VALUES ('4', '2014-09-08 07:36:53', '1', '8', '1', 'Label object', '3', '');
INSERT INTO `django_admin_log` VALUES ('5', '2014-09-08 08:55:07', '1', '8', '10', '', '3', '');
INSERT INTO `django_admin_log` VALUES ('6', '2014-09-08 09:24:03', '1', '9', '10', '201409081655', '3', '');
INSERT INTO `django_admin_log` VALUES ('7', '2014-09-08 09:24:03', '1', '9', '9', '201409081652', '3', '');
INSERT INTO `django_admin_log` VALUES ('8', '2014-09-08 09:24:03', '1', '9', '8', '201409081650', '3', '');
INSERT INTO `django_admin_log` VALUES ('9', '2014-09-08 09:24:03', '1', '9', '7', '201409081649', '3', '');
INSERT INTO `django_admin_log` VALUES ('10', '2014-09-08 09:24:03', '1', '9', '6', '201409081648', '3', '');
INSERT INTO `django_admin_log` VALUES ('11', '2014-09-08 09:24:03', '1', '9', '5', '201409081646', '3', '');
INSERT INTO `django_admin_log` VALUES ('12', '2014-09-08 09:24:03', '1', '9', '4', '201409081646', '3', '');
INSERT INTO `django_admin_log` VALUES ('13', '2014-09-08 09:24:04', '1', '9', '3', '标题', '3', '');
INSERT INTO `django_admin_log` VALUES ('14', '2014-09-08 09:24:04', '1', '9', '2', '123', '3', '');
INSERT INTO `django_admin_log` VALUES ('15', '2014-09-08 09:24:04', '1', '9', '1', '123', '3', '');
INSERT INTO `django_admin_log` VALUES ('16', '2014-09-08 15:31:29', '1', '9', '16', '第一篇博客，中秋快乐', '2', 'Changed raw_content and markdown_content.');
INSERT INTO `django_admin_log` VALUES ('17', '2014-09-08 15:32:17', '1', '9', '16', '第一篇博客，中秋快乐', '2', 'Changed raw_content and markdown_content.');
INSERT INTO `django_admin_log` VALUES ('18', '2014-09-08 15:33:24', '1', '9', '16', '第一篇博客，中秋快乐', '2', 'Changed markdown_content.');
INSERT INTO `django_admin_log` VALUES ('19', '2014-09-08 16:08:02', '1', '9', '16', '第一篇博客，中秋快乐', '2', 'Changed markdown_content.');
INSERT INTO `django_admin_log` VALUES ('20', '2014-09-08 16:08:28', '1', '9', '16', '第一篇博客，中秋快乐', '2', 'Changed markdown_content.');

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
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
INSERT INTO `django_content_type` VALUES ('7', 'migration history', 'south', 'migrationhistory');
INSERT INTO `django_content_type` VALUES ('8', 'label', 'article', 'label');
INSERT INTO `django_content_type` VALUES ('9', 'article', 'article', 'article');
INSERT INTO `django_content_type` VALUES ('10', 'labels in article', 'article', 'labelsinarticle');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('n5ejrz16vb6aqq7onnap1ig90c9wh8ri', 'OWUzNDUyYTE2MDZhNmVmZmQ1YWMwYmI1NDVlY2RiNWIzYWM5YzRjNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=', '2014-09-21 09:21:25');

-- ----------------------------
-- Table structure for `south_migrationhistory`
-- ----------------------------
DROP TABLE IF EXISTS `south_migrationhistory`;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of south_migrationhistory
-- ----------------------------
INSERT INTO `south_migrationhistory` VALUES ('1', 'article', '0001_initial', '2014-09-07 09:09:00');
INSERT INTO `south_migrationhistory` VALUES ('2', 'article', '0002_auto__add_field_label_number_is_used', '2014-09-08 09:23:54');
INSERT INTO `south_migrationhistory` VALUES ('3', 'article', '0003_auto__del_field_article_content__add_field_article_raw_content__add_fi', '2014-09-08 15:18:13');
INSERT INTO `south_migrationhistory` VALUES ('4', 'article', '0004_auto__add_field_article_abstract', '2014-09-08 16:18:36');
