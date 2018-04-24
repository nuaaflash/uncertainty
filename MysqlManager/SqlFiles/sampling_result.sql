/*
 Navicat Premium Data Transfer

 Source Server         : Ghost
 Source Server Type    : MySQL
 Source Server Version : 50173
 Source Host           : 118.89.198.205:3306
 Source Schema         : work

 Target Server Type    : MySQL
 Target Server Version : 50173
 File Encoding         : 65001

 Date: 21/04/2018 11:45:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sampling_result
-- ----------------------------
DROP TABLE IF EXISTS `sampling_result`;
CREATE TABLE `sampling_result`  (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `result_value` float(9, 3) NOT NULL,
  `sampling_method` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `distribution_type` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`result_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 939 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
