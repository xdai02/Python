DROP TABLE IF EXISTS info;

CREATE TABLE info(
    id int,
    name varchar(16),
    gpa double(5, 2)
);

INSERT INTO info VALUES
(1, "Terry", 3.7),
(2, "Lily", 4.2),
(3, "Eric", 3.3),
(4, "Alice", 3.6),
(5, "Lily", 4.2),
(6, "Terry", 3.7),
(7, "Anna", 4.1),
(8, "Jason", 3.9);