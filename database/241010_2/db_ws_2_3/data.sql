PRAGMA table_info('hotels');

-- 이거 없어서 안 되는거 같은데
DROP TABLE
  hotels;

CREATE TABLE hotels (
  room_num TEXT PRIMARY KEY, 
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL,
  grade TEXT NOT NULL
);

INSERT INTO hotels('room_num', 'check_in', 'check_out', 'grade')
VALUES
  ('101', '2024-03-20', '2024-03-25', 'standard'),
  ('202', '2024-03-21', '2024-03-24', 'deluxe'),
  ('303', '2024-03-22', '2024-03-26', 'suite'),
  ('404', '2024-03-23', '2024-03-27', 'penthouse')

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

-- FOREIGN KEY 관련한 것은 뒤로 미루고 콤마 안 찍는 듯
CREATE TABLE reservations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER,
  room_num TEXT,
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL,
    FOREIGN KEY (customer_id)
      REFERENCES customers(id)
    FOREIGN KEY (room_num)
      REFERENCES hotels(room_num)
);

INSERT INTO
  customers('name', 'email')
VALUES
  ('홍길동', 'john@example.com'),
  ('박지영', 'jane@example.com'),
  ('김미영', 'alice@example.com'),
  ('이철수', 'bob@example.com')

INSERT INTO
  reservations('customer_id', 'room_num', 'check_in', 'check_out')
VALUES
  (1, '101', '2024-03-20', '2024-03-25'),
  (2, '202', '2024-03-21', '2024-03-24'),
  (3, '303', '2024-03-22', '2024-03-26'),
  (4, '404', '2024-03-23', '2024-03-27')


SELECT * FROM customers

SELECT * FROM reservations;