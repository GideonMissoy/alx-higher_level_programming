-- Lists in DESC all genres in the DB by their rating.
SELECT `name`, SUM(`rate`) AS `rating`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s
ON s.`genre_id` = g.`id`

INNER JOIN `tv_show_ratings` AS r
ON r.`show_id` = s.`show_id`
GROUP BY `name`
ORDER BY `rating` DESC;
