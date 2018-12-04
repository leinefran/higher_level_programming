-- a script that lists all the cities of California that can be found
-- in the database hbtn_0d_usa.

SELECT
	cities.id, cities.name, states.name
FROM
	cities, states
ORDER BY
      cities.id ASC;
