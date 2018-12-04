-- a script that creates a table in the current database in your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1,
       name VARCHAR(256) NOT NULL,
       UNIQUE (id));
