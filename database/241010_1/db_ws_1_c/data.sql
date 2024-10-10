SELECT
  genre,
  COUNT(*) AS count
FROM
  songs
GROUP BY
  genre;

SELECT
  genre,
  COUNT(*) as count,
  AVG(duration) AS average_duration
FROM
  songs
GROUP BY
  genre;