-- all genres
WITH tmp_table AS ((SELECT tv_shows.title FROM tv_show_genres
JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
RIGHT JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title ASC)
EXCEPT
(SELECT tv_shows.title FROM tv_show_genres
JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
RIGHT JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
WHERE tv_genres.name='COMEDY'
ORDER BY tv_shows.title ASC))
SELECT tmp_table.title FROM tmp_table
ORDER BY tmp_table.title;