/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50614
Source Host           : 127.0.0.1:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50614
File Encoding         : 65001

Date: 2014-09-14 22:06:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `article_quicknote`
-- ----------------------------
DROP TABLE IF EXISTS `article_quicknote`;
CREATE TABLE `article_quicknote` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `note` longtext NOT NULL,
  `post_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article_quicknote
-- ----------------------------
INSERT INTO `article_quicknote` VALUES ('1', '1.工业化进展导致传统劳动业趋于饱和，劳动力转移非制造业，国家创造虚拟经济行业减缓失业压力。2.生产过剩，消费不足，经济的增长必须依靠消费来带动。前者导致金融产品及衍生物滋长，后者导致超前消费，损害经济正常发展', '2014-09-14 13:46:44');
