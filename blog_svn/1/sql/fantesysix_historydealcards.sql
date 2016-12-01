/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50614
Source Host           : 127.0.0.1:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50614
File Encoding         : 65001

Date: 2014-12-11 11:46:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `fantesysix_historydealcards`
-- ----------------------------
DROP TABLE IF EXISTS `fantesysix_historydealcards`;
CREATE TABLE `fantesysix_historydealcards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deal_cards` text NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fantesysix_historydealcards
-- ----------------------------
INSERT INTO `fantesysix_historydealcards` VALUES ('1', '[[{\'B\': 7}, {\'B\': 3}, {\'D\': 7}, {\'B\': 1}, {\'C\': 8}, {\'D\': 6}], [{\'B\': 9}, {\'D\': 4}, {\'D\': 8}, {\'B\': 4}, {\'A\': 13}, {\'D\': 12}]]', '2014-12-10 01:32:18');
INSERT INTO `fantesysix_historydealcards` VALUES ('2', '[[{\'C\': 2}, {\'B\': 12}, {\'D\': 10}, {\'D\': 12}, {\'A\': 11}, {\'A\': 2}], [{\'A\': 1}, {\'D\': 4}, {\'B\': 5}, {\'A\': 3}, {\'B\': 6}, {\'B\': 7}]]', '2014-12-10 01:55:20');
INSERT INTO `fantesysix_historydealcards` VALUES ('3', '[[{\'B\': 9}, {\'C\': 13}, {\'A\': 1}, {\'C\': 1}, {\'D\': 1}, {\'A\': 4}], [{\'C\': 9}, {\'C\': 7}, {\'B\': 1}, {\'B\': 13}, {\'A\': 11}, {\'D\': 10}]]', '2014-12-10 01:56:10');
INSERT INTO `fantesysix_historydealcards` VALUES ('4', '[[{\'D\': 5}, {\'B\': 9}, {\'B\': 13}, {\'A\': 8}, {\'A\': 11}, {\'D\': 4}], [{\'A\': 2}, {\'B\': 5}, {\'D\': 7}, {\'B\': 6}, {\'A\': 3}, {\'C\': 4}]]', '2014-12-10 01:57:00');
INSERT INTO `fantesysix_historydealcards` VALUES ('5', '[[{\'D\': 7}, {\'B\': 8}, {\'A\': 1}, {\'B\': 13}, {\'C\': 4}, {\'C\': 3}], [{\'C\': 5}, {\'A\': 3}, {\'B\': 12}, {\'D\': 5}, {\'C\': 10}, {\'B\': 2}]]', '2014-12-10 01:57:20');
INSERT INTO `fantesysix_historydealcards` VALUES ('6', '[[{\'C\': 5}, {\'A\': 8}, {\'D\': 9}, {\'C\': 2}, {\'D\': 6}, {\'D\': 1}], [{\'A\': 1}, {\'C\': 4}, {\'C\': 9}, {\'D\': 10}, {\'D\': 2}, {\'B\': 3}]]', '2014-12-10 02:08:47');
INSERT INTO `fantesysix_historydealcards` VALUES ('7', '[[{\'B\': 1}, {\'B\': 12}, {\'D\': 1}, {\'A\': 6}, {\'D\': 5}, {\'D\': 10}], [{\'B\': 2}, {\'D\': 6}, {\'C\': 2}, {\'C\': 6}, {\'B\': 13}, {\'B\': 7}]]', '2014-12-10 02:09:09');
INSERT INTO `fantesysix_historydealcards` VALUES ('8', '[[{\'C\': 2}, {\'A\': 11}, {\'A\': 7}, {\'C\': 13}, {\'A\': 8}, {\'A\': 5}], [{\'D\': 1}, {\'A\': 4}, {\'A\': 10}, {\'D\': 4}, {\'B\': 8}, {\'B\': 2}]]', '2014-12-10 02:10:53');
INSERT INTO `fantesysix_historydealcards` VALUES ('9', '[[{\'A\': 9}, {\'A\': 13}, {\'A\': 4}, {\'D\': 5}, {\'B\': 2}, {\'D\': 11}], [{\'C\': 6}, {\'C\': 10}, {\'A\': 3}, {\'D\': 3}, {\'C\': 7}, {\'C\': 2}]]', '2014-12-10 02:11:17');
INSERT INTO `fantesysix_historydealcards` VALUES ('10', '[[{\'A\': 5}, {\'B\': 5}, {\'A\': 9}, {\'D\': 1}, {\'B\': 4}, {\'C\': 7}], [{\'C\': 12}, {\'A\': 11}, {\'C\': 5}, {\'A\': 7}, {\'D\': 6}, {\'C\': 6}]]', '2014-12-10 02:11:41');
INSERT INTO `fantesysix_historydealcards` VALUES ('11', '[[{\'A\': 1}, {\'C\': 1}, {\'D\': 4}, {\'D\': 5}, {\'B\': 4}, {\'D\': 3}], [{\'A\': 4}, {\'A\': 11}, {\'D\': 7}, {\'C\': 6}, {\'B\': 6}, {\'D\': 10}]]', '2014-12-10 02:13:46');
INSERT INTO `fantesysix_historydealcards` VALUES ('12', '[[{\'C\': 3}, {\'C\': 6}, {\'B\': 11}, {\'C\': 2}, {\'B\': 7}, {\'C\': 9}], [{\'B\': 12}, {\'C\': 7}, {\'A\': 5}, {\'C\': 4}, {\'A\': 10}, {\'D\': 3}]]', '2014-12-10 02:35:43');
INSERT INTO `fantesysix_historydealcards` VALUES ('13', '[[{\'A\': 9}, {\'B\': 3}, {\'B\': 12}, {\'B\': 5}, {\'C\': 12}, {\'B\': 1}], [{\'C\': 13}, {\'C\': 10}, {\'A\': 13}, {\'C\': 2}, {\'C\': 1}, {\'C\': 9}]]', '2014-12-10 02:36:13');
INSERT INTO `fantesysix_historydealcards` VALUES ('14', '[[{\'D\': 6}, {\'B\': 10}, {\'D\': 12}, {\'A\': 5}, {\'C\': 12}, {\'C\': 11}], [{\'B\': 8}, {\'A\': 2}, {\'C\': 8}, {\'C\': 13}, {\'A\': 4}, {\'B\': 6}]]', '2014-12-10 02:36:42');
INSERT INTO `fantesysix_historydealcards` VALUES ('15', '[[{\'D\': 12}, {\'C\': 3}, {\'D\': 7}, {\'A\': 13}, {\'C\': 5}, {\'B\': 11}], [{\'A\': 11}, {\'C\': 11}, {\'A\': 5}, {\'A\': 8}, {\'C\': 6}, {\'C\': 12}]]', '2014-12-10 02:37:27');
INSERT INTO `fantesysix_historydealcards` VALUES ('16', '[[{\'A\': 1}, {\'B\': 7}, {\'B\': 5}, {\'A\': 12}, {\'C\': 2}, {\'B\': 2}], [{\'D\': 1}, {\'C\': 8}, {\'A\': 4}, {\'A\': 11}, {\'D\': 10}, {\'C\': 12}]]', '2014-12-10 02:37:59');
INSERT INTO `fantesysix_historydealcards` VALUES ('17', '[[{\'A\': 12}, {\'D\': 11}, {\'B\': 9}, {\'C\': 3}, {\'D\': 4}, {\'D\': 2}], [{\'A\': 3}, {\'B\': 7}, {\'D\': 7}, {\'C\': 4}, {\'D\': 8}, {\'B\': 1}]]', '2014-12-10 02:38:23');
INSERT INTO `fantesysix_historydealcards` VALUES ('18', '[[{\'D\': 6}, {\'C\': 10}, {\'D\': 11}, {\'D\': 12}, {\'C\': 6}, {\'D\': 2}], [{\'B\': 6}, {\'B\': 13}, {\'B\': 3}, {\'A\': 6}, {\'B\': 4}, {\'C\': 8}]]', '2014-12-10 02:39:13');
INSERT INTO `fantesysix_historydealcards` VALUES ('19', '[[{\'C\': 5}, {\'A\': 12}, {\'C\': 3}, {\'C\': 2}, {\'A\': 10}, {\'B\': 13}], [{\'D\': 12}, {\'C\': 12}, {\'D\': 3}, {\'B\': 1}, {\'B\': 2}, {\'A\': 8}]]', '2014-12-10 02:39:37');
INSERT INTO `fantesysix_historydealcards` VALUES ('20', '[[{\'C\': 3}, {\'C\': 2}, {\'A\': 3}, {\'C\': 11}, {\'D\': 12}, {\'D\': 6}], [{\'A\': 5}, {\'A\': 8}, {\'C\': 10}, {\'C\': 7}, {\'B\': 5}, {\'D\': 11}]]', '2014-12-10 02:40:27');
INSERT INTO `fantesysix_historydealcards` VALUES ('21', '[[{\'A\': 9}, {\'B\': 6}, {\'A\': 8}, {\'C\': 5}, {\'C\': 12}, {\'C\': 8}], [{\'B\': 7}, {\'B\': 12}, {\'D\': 2}, {\'B\': 13}, {\'C\': 11}, {\'C\': 13}]]', '2014-12-10 03:00:12');
INSERT INTO `fantesysix_historydealcards` VALUES ('22', '[[{\'D\': 2}, {\'B\': 2}, {\'A\': 3}, {\'A\': 13}, {\'D\': 6}, {\'B\': 4}], [{\'C\': 6}, {\'C\': 12}, {\'D\': 3}, {\'D\': 11}, {\'C\': 7}, {\'C\': 11}]]', '2014-12-10 03:01:43');
INSERT INTO `fantesysix_historydealcards` VALUES ('23', '[[{\'A\': 12}, {\'D\': 5}, {\'B\': 4}, {\'D\': 10}, {\'A\': 2}, {\'C\': 7}], [{\'A\': 8}, {\'C\': 8}, {\'C\': 12}, {\'B\': 7}, {\'B\': 11}, {\'D\': 9}]]', '2014-12-10 03:02:35');
INSERT INTO `fantesysix_historydealcards` VALUES ('24', '[[{\'C\': 7}, {\'B\': 6}, {\'D\': 6}, {\'B\': 8}, {\'C\': 13}, {\'B\': 5}], [{\'D\': 9}, {\'D\': 4}, {\'B\': 12}, {\'A\': 9}, {\'D\': 5}, {\'C\': 10}]]', '2014-12-10 03:03:11');
