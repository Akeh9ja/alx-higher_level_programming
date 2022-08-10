-- group by in sql to count the number of scores
SELECT score, COUNT(score) 'number' FROM second_table GROUP BY score ORDER BY number DESC; 