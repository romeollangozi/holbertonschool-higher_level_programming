-- task 13
SELECT gen.name AS genre, COUNT(*) AS number_of_shows FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres.show_id=tv_shows.id
JOIN tv_genres AS gen
ON gen.id=tv_show_genres.genre_id
GROUP BY gen.name
ORDER BY number_of_shows DESC;