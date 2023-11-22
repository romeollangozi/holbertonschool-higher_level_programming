-- ratings
SELECT tv_genres.name, SUM(tv_show_ratings.rate)
AS rating
FROM tv_show_ratings
JOIN tv_shows ON tv_shows.id=tv_show_ratings.show_id
JOIN tv_show_genres ON tv_show_genres.show_id=tv_shows.id
JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
GROUP BY tv_genres.name
ORDER BY rating DESC;
