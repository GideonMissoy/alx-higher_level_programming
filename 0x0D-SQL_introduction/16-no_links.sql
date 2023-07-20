-- Lists in DESC all records of table having a name value.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ''
ORDER BY `score` DESC
