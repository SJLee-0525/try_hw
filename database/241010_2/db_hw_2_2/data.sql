PRAGMA table_info('data');

CREATE TABLE orders(
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date DATE,
  total_amount REAL
);

INSERT INTO
  orders('order_date', 'total_amount')
VALUES
  ('2023-07-15', 50.99),
  ('2023-07-16', 75.5),
  ('2023-07-17', 30.25)

CREATE TABLE customers (
  customie_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL
);

INSERT INTO
  customers ('name', 'email', 'phone')
VALUES
  ('허균', 'hong.gildong@example.com', '010-1234-1234'),
  ('김영희', 'kim.younghee@example.com', '010-4212-1134'),
  ('이철수', 'lee.cheolsu@example.com', '010-5555-4444')

DELETE FROM
  orders
WHERE
  order_id = 3;


UPDATE
  customers
SET
  name = '홍길동'
WHERE
  customie_id = 1;

SELECT * FROM orders;

SELECT * FROM customers