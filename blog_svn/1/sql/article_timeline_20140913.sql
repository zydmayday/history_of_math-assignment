/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50614
Source Host           : 127.0.0.1:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50614
File Encoding         : 65001

Date: 2014-09-13 00:59:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `article_timeline`
-- ----------------------------
DROP TABLE IF EXISTS `article_timeline`;
CREATE TABLE `article_timeline` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `tag` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article_timeline
-- ----------------------------
INSERT INTO `article_timeline` VALUES ('1', '2013-01-01', '123', 'hahaah');
INSERT INTO `article_timeline` VALUES ('2', '2013-02-01', '345', 'fdsgsf ');
INSERT INTO `article_timeline` VALUES ('3', '2013-01-02', '234', '12312312312');
INSERT INTO `article_timeline` VALUES ('4', '2014-08-09', '456', 'asdfasdf');
INSERT INTO `article_timeline` VALUES ('5', '2013-01-03', '123', 'dsf');
INSERT INTO `article_timeline` VALUES ('6', '2013-01-04', 'dfsd', '231231');
INSERT INTO `article_timeline` VALUES ('7', '2013-01-05', 'dsf', '123');
INSERT INTO `article_timeline` VALUES ('8', '2013-01-06', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('9', '2013-01-07', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('10', '2013-01-08', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('11', '2013-01-09', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('12', '2013-01-10', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('13', '2013-01-11', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('14', '2013-01-12', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('15', '2013-01-13', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('16', '2013-01-14', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('17', '2013-01-15', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('18', '2013-01-16', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('19', '2013-01-17', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('20', '2013-01-18', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('21', '2013-01-19', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('22', '2013-01-20', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('23', '2013-01-21', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('24', '2013-01-22', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('25', '2013-01-23', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('26', '2013-01-24', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('27', '2013-01-25', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('28', '2013-01-26', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('29', '2013-01-27', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('30', '2013-01-28', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('31', '2013-01-29', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('32', '2013-01-30', 'ddd', '222');
INSERT INTO `article_timeline` VALUES ('33', '2013-02-01', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('34', '2013-02-02', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('35', '2013-02-03', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('36', '2013-02-04', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('37', '2013-02-05', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('38', '2013-02-06', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('39', '2013-02-07', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('40', '2013-02-08', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('41', '2013-02-09', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('42', '2013-02-10', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('43', '2013-02-11', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('44', '2013-02-12', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('45', '2013-02-13', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('46', '2013-02-14', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('47', '2013-02-15', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('48', '2013-02-16', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('49', '2013-02-17', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('50', '2013-02-18', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('51', '2013-02-19', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('52', '2013-02-20', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('53', '2013-02-21', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('54', '2013-02-22', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('55', '2013-02-23', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('56', '2013-02-24', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('57', '2013-02-25', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('58', '2013-02-26', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('59', '2013-02-27', '标签打的', '222');
INSERT INTO `article_timeline` VALUES ('60', '2013-03-01', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('61', '2013-03-02', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('62', '2013-03-03', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('63', '2013-03-04', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('64', '2013-03-05', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('65', '2013-03-06', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('66', '2013-03-07', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('67', '2013-03-08', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('68', '2013-03-09', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('69', '2013-03-10', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('70', '2013-03-11', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('71', '2013-03-12', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('72', '2013-03-13', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('73', '2013-03-14', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('74', '2013-03-15', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('75', '2013-03-16', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('76', '2013-03-17', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('77', '2013-03-18', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('78', '2013-03-19', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('79', '2013-03-20', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('80', '2013-03-21', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('81', '2013-03-22', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('82', '2013-03-23', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('83', '2013-03-24', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('84', '2013-03-25', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('85', '2013-03-26', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('86', '2013-03-27', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('87', '2013-03-28', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('88', '2013-03-29', '阿斯蒂芬', '222');
INSERT INTO `article_timeline` VALUES ('89', '2013-03-30', '阿斯蒂芬', '222');
