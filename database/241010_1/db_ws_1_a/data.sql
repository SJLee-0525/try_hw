PRAGMA table_info('songs');

CREATE TABLE songs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  artist TEXT NOT NULL,
  album TEXT NOT NULL,
  genre TEXT NOT NULL,
  duration INTEGER
);

INSERT INTO 
  songs ('title', 'artist', 'album', 'genre', 'duration')
VALUES
  ('Song1', 'Artist1', 'Album1', 'POP', 200),
  ('Song2', 'Artist2', 'Album2', 'Rock', 300),
  ('Song3', 'Artist3', 'Album3', 'Hip Hop', 250),
  ('Song4', 'Artist4', 'Album4', 'Electoronic', 180),
  ('Song5', 'Artist5', 'Album5', 'R&B', 320)

UPDATE
  songs
SET 
  title = 'New Title'
WHERE
  id = 1;