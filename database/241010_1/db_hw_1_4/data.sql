SELECT
  *
FROM
  tracks
WHERE
  Name LIKE '%love%'

SELECT
  *
FROM
  tracks
WHERE
  GenreID = 1
  AND Milliseconds >= 300000
ORDER BY
  UnitPrice DESC;

SELECT
  GenreID,
  COUNT(*) AS 'TotalTracks'
FROM
  tracks
GROUP BY
  GenreID;

SELECT
  GenreID,
  SUM(UnitPrice) AS 'TotalPrice'
FROM
  tracks
GROUP BY
  GenreId
HAVING
  TotalPrice >= 100;