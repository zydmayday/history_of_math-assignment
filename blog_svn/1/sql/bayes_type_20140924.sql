/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50614
Source Host           : 127.0.0.1:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50614
File Encoding         : 65001

Date: 2014-09-24 17:26:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `bayes_type`
-- ----------------------------
DROP TABLE IF EXISTS `bayes_type`;
CREATE TABLE `bayes_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `total_count` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bayes_type
-- ----------------------------
INSERT INTO `bayes_type` VALUES ('15', 'china', '8');
INSERT INTO `bayes_type` VALUES ('16', 'japan', '3');
