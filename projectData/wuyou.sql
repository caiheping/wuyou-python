/*
 Navicat Premium Data Transfer

 Source Server         : cai
 Source Server Type    : MySQL
 Source Server Version : 80016
 Source Host           : localhost:3306
 Source Schema         : wuyou

 Target Server Type    : MySQL
 Target Server Version : 80016
 File Encoding         : 65001

 Date: 12/09/2019 16:02:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 65 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add 用户', 6, 'add_users');
INSERT INTO `auth_permission` VALUES (22, 'Can change 用户', 6, 'change_users');
INSERT INTO `auth_permission` VALUES (23, 'Can delete 用户', 6, 'delete_users');
INSERT INTO `auth_permission` VALUES (24, 'Can view 用户', 6, 'view_users');
INSERT INTO `auth_permission` VALUES (25, 'Can add 公司', 7, 'add_companys');
INSERT INTO `auth_permission` VALUES (26, 'Can change 公司', 7, 'change_companys');
INSERT INTO `auth_permission` VALUES (27, 'Can delete 公司', 7, 'delete_companys');
INSERT INTO `auth_permission` VALUES (28, 'Can view 公司', 7, 'view_companys');
INSERT INTO `auth_permission` VALUES (29, 'Can add 福利', 8, 'add_welfare');
INSERT INTO `auth_permission` VALUES (30, 'Can change 福利', 8, 'change_welfare');
INSERT INTO `auth_permission` VALUES (31, 'Can delete 福利', 8, 'delete_welfare');
INSERT INTO `auth_permission` VALUES (32, 'Can view 福利', 8, 'view_welfare');
INSERT INTO `auth_permission` VALUES (33, 'Can add 职业', 9, 'add_job');
INSERT INTO `auth_permission` VALUES (34, 'Can change 职业', 9, 'change_job');
INSERT INTO `auth_permission` VALUES (35, 'Can delete 职业', 9, 'delete_job');
INSERT INTO `auth_permission` VALUES (36, 'Can view 职业', 9, 'view_job');
INSERT INTO `auth_permission` VALUES (37, 'Can add 简历', 10, 'add_resume');
INSERT INTO `auth_permission` VALUES (38, 'Can change 简历', 10, 'change_resume');
INSERT INTO `auth_permission` VALUES (39, 'Can delete 简历', 10, 'delete_resume');
INSERT INTO `auth_permission` VALUES (40, 'Can view 简历', 10, 'view_resume');
INSERT INTO `auth_permission` VALUES (41, 'Can add 工作经验', 11, 'add_resumeworking');
INSERT INTO `auth_permission` VALUES (42, 'Can change 工作经验', 11, 'change_resumeworking');
INSERT INTO `auth_permission` VALUES (43, 'Can delete 工作经验', 11, 'delete_resumeworking');
INSERT INTO `auth_permission` VALUES (44, 'Can view 工作经验', 11, 'view_resumeworking');
INSERT INTO `auth_permission` VALUES (45, 'Can add 项目经验', 12, 'add_resumeprojectexperience');
INSERT INTO `auth_permission` VALUES (46, 'Can change 项目经验', 12, 'change_resumeprojectexperience');
INSERT INTO `auth_permission` VALUES (47, 'Can delete 项目经验', 12, 'delete_resumeprojectexperience');
INSERT INTO `auth_permission` VALUES (48, 'Can view 项目经验', 12, 'view_resumeprojectexperience');
INSERT INTO `auth_permission` VALUES (49, 'Can add 求职意向', 13, 'add_resumejob');
INSERT INTO `auth_permission` VALUES (50, 'Can change 求职意向', 13, 'change_resumejob');
INSERT INTO `auth_permission` VALUES (51, 'Can delete 求职意向', 13, 'delete_resumejob');
INSERT INTO `auth_permission` VALUES (52, 'Can view 求职意向', 13, 'view_resumejob');
INSERT INTO `auth_permission` VALUES (53, 'Can add 教育经历', 14, 'add_resumeeducation');
INSERT INTO `auth_permission` VALUES (54, 'Can change 教育经历', 14, 'change_resumeeducation');
INSERT INTO `auth_permission` VALUES (55, 'Can delete 教育经历', 14, 'delete_resumeeducation');
INSERT INTO `auth_permission` VALUES (56, 'Can view 教育经历', 14, 'view_resumeeducation');
INSERT INTO `auth_permission` VALUES (57, 'Can add 轮播图', 15, 'add_banner');
INSERT INTO `auth_permission` VALUES (58, 'Can change 轮播图', 15, 'change_banner');
INSERT INTO `auth_permission` VALUES (59, 'Can delete 轮播图', 15, 'delete_banner');
INSERT INTO `auth_permission` VALUES (60, 'Can view 轮播图', 15, 'view_banner');
INSERT INTO `auth_permission` VALUES (61, 'Can add 区域', 16, 'add_areainfo');
INSERT INTO `auth_permission` VALUES (62, 'Can change 区域', 16, 'change_areainfo');
INSERT INTO `auth_permission` VALUES (63, 'Can delete 区域', 16, 'delete_areainfo');
INSERT INTO `auth_permission` VALUES (64, 'Can view 区域', 16, 'view_areainfo');

-- ----------------------------
-- Table structure for base_areainfo
-- ----------------------------
DROP TABLE IF EXISTS `base_areainfo`;
CREATE TABLE `base_areainfo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `atitle` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `aParent_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `base_areainfo_aParent_id_96b375a7_fk_base_areainfo_id`(`aParent_id`) USING BTREE,
  CONSTRAINT `base_areainfo_aParent_id_96b375a7_fk_base_areainfo_id` FOREIGN KEY (`aParent_id`) REFERENCES `base_areainfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for base_banner
-- ----------------------------
DROP TABLE IF EXISTS `base_banner`;
CREATE TABLE `base_banner`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_delete` tinyint(1) NOT NULL,
  `index` int(11) NOT NULL,
  `image` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `url` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for companys_companys
-- ----------------------------
DROP TABLE IF EXISTS `companys_companys`;
CREATE TABLE `companys_companys`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `type` int(11) NOT NULL,
  `addr` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `area` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `introduce` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `personnel` int(11) NOT NULL,
  `company_start_time` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for companys_job
-- ----------------------------
DROP TABLE IF EXISTS `companys_job`;
CREATE TABLE `companys_job`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_delete` tinyint(1) NOT NULL,
  `job` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `min_salary` int(11) NOT NULL,
  `max_salary` int(11) NOT NULL,
  `describe` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `working_years` int(11) NOT NULL,
  `education` int(11) NOT NULL,
  `recruitment` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `companys_job_company_id_f9579152_fk_companys_companys_id`(`company_id`) USING BTREE,
  CONSTRAINT `companys_job_company_id_f9579152_fk_companys_companys_id` FOREIGN KEY (`company_id`) REFERENCES `companys_companys` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for companys_welfare
-- ----------------------------
DROP TABLE IF EXISTS `companys_welfare`;
CREATE TABLE `companys_welfare`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `company_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `companys_welfare_company_id_88743a69_fk_companys_companys_id`(`company_id`) USING BTREE,
  CONSTRAINT `companys_welfare_company_id_88743a69_fk_companys_companys_id` FOREIGN KEY (`company_id`) REFERENCES `companys_companys` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_df_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2019-09-12 07:11:44.656375', '2', '小菜', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (2, '2019-09-12 07:12:15.849671', '2', '小菜', 2, '[]', 6, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (16, 'base', 'areainfo');
INSERT INTO `django_content_type` VALUES (15, 'base', 'banner');
INSERT INTO `django_content_type` VALUES (7, 'companys', 'companys');
INSERT INTO `django_content_type` VALUES (9, 'companys', 'job');
INSERT INTO `django_content_type` VALUES (8, 'companys', 'welfare');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (10, 'resumes', 'resume');
INSERT INTO `django_content_type` VALUES (14, 'resumes', 'resumeeducation');
INSERT INTO `django_content_type` VALUES (13, 'resumes', 'resumejob');
INSERT INTO `django_content_type` VALUES (12, 'resumes', 'resumeprojectexperience');
INSERT INTO `django_content_type` VALUES (11, 'resumes', 'resumeworking');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (6, 'users', 'users');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 26 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2019-09-12 06:59:47.890039');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2019-09-12 06:59:47.943896');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2019-09-12 06:59:47.999774');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2019-09-12 06:59:48.137378');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2019-09-12 06:59:48.143362');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2019-09-12 06:59:48.149346');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2019-09-12 06:59:48.156328');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2019-09-12 06:59:48.159323');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2019-09-12 06:59:48.165303');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2019-09-12 06:59:48.171288');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2019-09-12 06:59:48.178293');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0010_alter_group_name_max_length', '2019-09-12 06:59:48.214172');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0011_update_proxy_permissions', '2019-09-12 06:59:48.237146');
INSERT INTO `django_migrations` VALUES (14, 'users', '0001_initial', '2019-09-12 06:59:48.305927');
INSERT INTO `django_migrations` VALUES (15, 'admin', '0001_initial', '2019-09-12 06:59:48.470512');
INSERT INTO `django_migrations` VALUES (16, 'admin', '0002_logentry_remove_auto_add', '2019-09-12 06:59:48.545286');
INSERT INTO `django_migrations` VALUES (17, 'admin', '0003_logentry_add_action_flag_choices', '2019-09-12 06:59:48.553265');
INSERT INTO `django_migrations` VALUES (18, 'base', '0001_initial', '2019-09-12 06:59:48.592161');
INSERT INTO `django_migrations` VALUES (19, 'companys', '0001_initial', '2019-09-12 06:59:48.689900');
INSERT INTO `django_migrations` VALUES (20, 'companys', '0002_auto_20190912_1459', '2019-09-12 06:59:48.789633');
INSERT INTO `django_migrations` VALUES (21, 'resumes', '0001_initial', '2019-09-12 06:59:48.928262');
INSERT INTO `django_migrations` VALUES (22, 'resumes', '0002_resume_user', '2019-09-12 06:59:49.085841');
INSERT INTO `django_migrations` VALUES (23, 'resumes', '0003_auto_20190912_1459', '2019-09-12 06:59:49.165627');
INSERT INTO `django_migrations` VALUES (24, 'sessions', '0001_initial', '2019-09-12 06:59:49.184576');
INSERT INTO `django_migrations` VALUES (25, 'users', '0002_auto_20190912_1459', '2019-09-12 06:59:49.246411');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('1cr0ebvu7k23qiy5j8rzsgdrp1lopks7', 'ZTMzNzg5NzRhMWViZDk4YTdiYWQ4MGU0Y2VlMTA1YTE3MDQxMjljYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmZGM1ZTVlNzViZDFmZmY1YmYxZjc2NWJiYTM4NjJhYjNmZWI2NjE2In0=', '2019-09-26 07:02:22.316566');

-- ----------------------------
-- Table structure for resumes_resume
-- ----------------------------
DROP TABLE IF EXISTS `resumes_resume`;
CREATE TABLE `resumes_resume`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_open` int(11) NOT NULL,
  `progress` int(11) NOT NULL,
  `username` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `img` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` varchar(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `birthday` date NULL DEFAULT NULL,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `status` int(11) NOT NULL,
  `start_working` date NULL DEFAULT NULL,
  `addr` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ID_number` varchar(18) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `annual_income` int(11) NOT NULL,
  `hukou_or_nationality` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `marital_status` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `resumes_resume_user_id_0221d0a3_fk_df_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `resumes_resume_user_id_0221d0a3_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for resumes_resumeeducation
-- ----------------------------
DROP TABLE IF EXISTS `resumes_resumeeducation`;
CREATE TABLE `resumes_resumeeducation`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_delete` tinyint(1) NOT NULL,
  `enrollment_time` date NOT NULL,
  `graduation_time` date NOT NULL,
  `school` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `education` int(11) NOT NULL,
  `major` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `major_desc` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_overseas_study` int(11) NOT NULL,
  `resume_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `resumes_resumeeducation_resume_id_458e42ce_fk_resumes_resume_id`(`resume_id`) USING BTREE,
  CONSTRAINT `resumes_resumeeducation_resume_id_458e42ce_fk_resumes_resume_id` FOREIGN KEY (`resume_id`) REFERENCES `resumes_resume` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for resumes_resumejob
-- ----------------------------
DROP TABLE IF EXISTS `resumes_resumejob`;
CREATE TABLE `resumes_resumejob`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_delete` tinyint(1) NOT NULL,
  `place` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `function` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pay_type` int(11) NOT NULL,
  `salary_expectation` int(11) NOT NULL,
  `work_type` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `industry` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `arrival_time` int(11) NOT NULL,
  `self_evaluation` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `personal_tags` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `resume_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `resumes_resumejob_resume_id_e2a564f7_fk_resumes_resume_id`(`resume_id`) USING BTREE,
  CONSTRAINT `resumes_resumejob_resume_id_e2a564f7_fk_resumes_resume_id` FOREIGN KEY (`resume_id`) REFERENCES `resumes_resume` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for resumes_resumeprojectexperience
-- ----------------------------
DROP TABLE IF EXISTS `resumes_resumeprojectexperience`;
CREATE TABLE `resumes_resumeprojectexperience`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_delete` tinyint(1) NOT NULL,
  `start_time` date NOT NULL,
  `end_time` date NOT NULL,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `project_description` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `responsibility_description` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `affiliated_company` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `resume_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `resumes_resumeprojec_resume_id_0ebb3240_fk_resumes_r`(`resume_id`) USING BTREE,
  CONSTRAINT `resumes_resumeprojec_resume_id_0ebb3240_fk_resumes_r` FOREIGN KEY (`resume_id`) REFERENCES `resumes_resume` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for resumes_resumeworking
-- ----------------------------
DROP TABLE IF EXISTS `resumes_resumeworking`;
CREATE TABLE `resumes_resumeworking`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_delete` tinyint(1) NOT NULL,
  `start_time` date NOT NULL,
  `end_time` date NOT NULL,
  `company` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `position` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `job_description` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `industry` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `department` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `nature` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `other` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `resume_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `resumes_resumeworking_resume_id_2b258ef0_fk_resumes_resume_id`(`resume_id`) USING BTREE,
  CONSTRAINT `resumes_resumeworking_resume_id_2b258ef0_fk_resumes_resume_id` FOREIGN KEY (`resume_id`) REFERENCES `resumes_resume` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for users_users
-- ----------------------------
DROP TABLE IF EXISTS `users_users`;
CREATE TABLE `users_users`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NULL,
  `create_time` datetime(6) NULL,
  `update_time` datetime(6) NULL,
  `is_delete` tinyint(1) NOT NULL,
  `area` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users_users
-- ----------------------------
INSERT INTO `users_users` VALUES (1, 'pbkdf2_sha256$150000$3mDEBzH5Eyi1$BzPNGdf9stPJr/ueN4owoHSUV3zPmxsGad05jzjlLLo=', '2019-09-12 07:02:22.307590', 1, 'admin', '', '', '123@qq.com', 1, 1, '2019-09-12 07:01:57.858708', '2019-09-12 07:01:58.042217', '2019-09-12 07:01:58.042217', 0, NULL);
INSERT INTO `users_users` VALUES (2, 'pbkdf2_sha256$150000$7SysrC4wPxDZ$uxvLhVfNvRUSoMoMDrM3vd6v2P1jAjkkB3q2W9wDWiw=', NULL, 0, '小菜', '', '', '', 0, 1, '2019-09-12 07:11:00.000000', '2019-09-12 07:11:44.654378', '2019-09-12 07:12:15.832689', 0, NULL);

-- ----------------------------
-- Table structure for users_users_groups
-- ----------------------------
DROP TABLE IF EXISTS `users_users_groups`;
CREATE TABLE `users_users_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `users_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `df_user_groups_users_id_group_id_87546692_uniq`(`users_id`, `group_id`) USING BTREE,
  INDEX `df_user_groups_group_id_36f24e94_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `df_user_groups_group_id_36f24e94_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `df_user_groups_users_id_0885f499_fk_df_user_id` FOREIGN KEY (`users_id`) REFERENCES `users_users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for users_users_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `users_users_user_permissions`;
CREATE TABLE `users_users_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `users_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `df_user_user_permissions_users_id_permission_id_bacb0432_uniq`(`users_id`, `permission_id`) USING BTREE,
  INDEX `df_user_user_permiss_permission_id_40a6cb2d_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `df_user_user_permiss_permission_id_40a6cb2d_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `df_user_user_permissions_users_id_6c09403c_fk_df_user_id` FOREIGN KEY (`users_id`) REFERENCES `users_users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
