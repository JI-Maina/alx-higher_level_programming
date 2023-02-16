-- reates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- columns id, state_id, name
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- open database
USE hbtn_0d_usa;
-- create cities table
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
