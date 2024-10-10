ALTER TABLE
  zoos
ADD COLUMN
  species TEXT NOT NULL;

UPDATE
  zoo
SET
  species = 'Panthera leo'
WHERE
  id = 1;


-- 다 되어있는데요....?