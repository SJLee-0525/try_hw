PRAGMA table_info('hotels');

SELECT * FROM hotels

UPDATE
  hotels
SET
  grade = upper(grade);

SELECT grade FROM hotels

CREATE TABLE customers(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL
)


CREATE TABLE reservations(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER,
    FOREIGN KEY (customer_id)
      REFERENCES customers(id)
  room_num TEXT,
    FOREIGN KEY (room_num)
      REFERENCE hotels(room_num)
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL
)