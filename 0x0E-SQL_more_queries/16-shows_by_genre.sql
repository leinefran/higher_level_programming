-- a script that lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.

SELECT
	tv_shows.title, tv_genres.name
FROM
	tv_shows
FULL JOIN
     tv_genres
ON
	tv_shows.title = tv_genres.name
WHERE
	tv_genres.name IS NULL
ORDER BY
      tv_shows.title DESC, tv_genres.name DESC;
