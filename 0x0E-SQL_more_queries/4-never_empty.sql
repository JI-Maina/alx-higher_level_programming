-- Creates the table id_not_null on your MySQL server with columns id & name
-- id should have a default value of 1
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
