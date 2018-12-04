-- a script that lists all shows contained in hbtn_0d_tvshows;
-- that have at least one genre linked.

SELECT
	title, genre_id
FROM
	tv_shows, tv_show_genres
ORDER BY
      tv_shows.title ASC, tv_show_genres.genre_id ASC;
