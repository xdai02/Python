DROP TABLE IF EXISTS info;

CREATE TABLE info(
	id int,
	name varchar(20),
	age int unsigned CHECK(age > 0)
);

DESC info;