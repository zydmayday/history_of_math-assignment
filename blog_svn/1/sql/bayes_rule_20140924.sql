/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50614
Source Host           : 127.0.0.1:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50614
File Encoding         : 65001

Date: 2014-09-24 17:26:27
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `bayes_rule`
-- ----------------------------
DROP TABLE IF EXISTS `bayes_rule`;
CREATE TABLE `bayes_rule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feature` varchar(100) NOT NULL,
  `count` double NOT NULL,
  `type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bayes_rule_403d8ff3` (`type_id`),
  CONSTRAINT `type_id_refs_id_a43fe6d1` FOREIGN KEY (`type_id`) REFERENCES `bayes_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=350 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bayes_rule
-- ----------------------------
INSERT INTO `bayes_rule` VALUES ('343', 'Chinese', '5', '15');
INSERT INTO `bayes_rule` VALUES ('344', 'Beijing', '1', '15');
INSERT INTO `bayes_rule` VALUES ('345', 'Shanghai', '1', '15');
INSERT INTO `bayes_rule` VALUES ('346', 'Macao', '1', '15');
INSERT INTO `bayes_rule` VALUES ('347', 'Tokyo', '1', '16');
INSERT INTO `bayes_rule` VALUES ('348', 'Japan', '1', '16');
INSERT INTO `bayes_rule` VALUES ('349', 'Chinese', '1', '16');
