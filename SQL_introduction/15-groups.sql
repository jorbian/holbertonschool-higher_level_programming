-- Script that lists number of records with same score in table 'second_table'
-- of the database
SELECT score 'score', COUNT(score) 'number' FROM second_table GROUP BY score ORDER BY COUNT(score) DESC;
