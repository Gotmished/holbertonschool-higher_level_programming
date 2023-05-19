-- Task ten: List all shows in hbtn_0d_tvshows
-- with at least one genre linked
SELECT
	tv_shows.title,
	tv_show_genres.genre_id
FROM tv_shows
RIGHT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, genre_id ASC;
-- Left join was bringing up programmes without genres.
-- Right join found only programs with genres listed.
