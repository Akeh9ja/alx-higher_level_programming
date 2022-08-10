-- Write a script that lists all records of the table second_table of the database 
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- Insert new values
INSERT INTO second_table (`id`, `name`, `score`) VALUES (6, 'Aria', 18);
INSERT INTO second_table (`id`, `name`, `score`) VALUES (7, 'Aria', 12);
-- listing rows and column
SELECT score, name FROM second_table ORDER BY score DESC;