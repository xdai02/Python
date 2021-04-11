-- 判断user表是否存在，如果存在则删除
DROP TABLE IF EXISTS user;

CREATE TABLE user(
    uid BIGINT AUTO_INCREMENT COMMENT '主键列（自动增长）',
    name VARCHAR(30) COMMENT '姓名',
    age INT COMMENT '年龄',
    height FLOAT COMMENT '身高',
    birth DATE COMMENT '生日',
    note TEXT COMMENT '备注',
    CONSTRAINT pk_uid PRIMARY KEY(uid)
) engine=INNODB;