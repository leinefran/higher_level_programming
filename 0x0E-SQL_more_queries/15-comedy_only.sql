-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT
	tv_shows.title
FROM
	tv_shows
LEFT OUTER JOIN	tv_genres

ON
	tv_shows.title = tv_genres.name
WHERE
	tv_gente.name = Comedy
ORDER BY
      tv_shows.title ASC;
