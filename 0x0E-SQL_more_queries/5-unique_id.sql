-- Write a script that creates the table unique_id on your MySQL server.
-- attach Unique
REATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));