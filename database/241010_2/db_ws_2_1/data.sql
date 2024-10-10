CREATE TABLE zoo(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT NOT NULL,
  age INT NOT NULL
);

INSERT INTO zoo('name', 'eat', 'weight', 'height', 'age')
VALUES
  ('Lion', 'Meat', 200, 120, 5),
  ('Elephant', 'Plants', 5000, 300, 15),
  ('Giraffe', 'Leaves', 1500, 550, 8),
  ('Monkey', 'Fruits', 50, 60, 10);

  SELECT * FROM zoo;