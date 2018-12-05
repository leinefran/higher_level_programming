-- a script that uses the hbtn_0d_tvshows database to lists all genres
-- of the show Dexter.

SELECT
	tv_genres.name
FROM
	tv_genres
RIGHT OUTER JOIN tv_shows

ON tv_shows.title = tv_genres.name

WHERE
	tv_show.title = Dexter
ORDER BY
      tv_genres.name ASC;
