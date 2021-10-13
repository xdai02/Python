DROP TABLE IF EXISTS info;

CREATE TABLE info(
    id int PRIMARY KEY,
    name varchar(16) NOT NULL,
    gpa double(5, 2) DEFAULT 0
);

DESC info;