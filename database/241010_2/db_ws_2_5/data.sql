SELECT 
    departments.name AS department,
    employees.name AS oldest_employee,
    MAX(employees.age) AS max_age,
    AVG(employees.age) AS avg_age 
FROM
    employees
INNER JOIN departments
    ON employees.departmentId = departments.id
    GROUP BY
        employees.departmentId;
    ORDER BY
        max_age ASC


SELECT
    departments.name AS department,
    employees.name AS higest_paid_employee,
    MAX(employees.salary) AS max_salary
FROM
    employees
INNER JOIN departments
    ON employees.departmentId = departments.id
    GROUP BY 
        departments.id;


SELECT 
    departments.name AS department,
    CASE 
        WHEN employees.age < 30 THEN 'Under 30'
        WHEN employees.age BETWEEN 30 AND 40 THEN 'BETWEEN 30-40'
        ELSE 'Over 40'
    END AS age_group,
    COUNT(*) AS num_employees
FROM employees
INNER JOIN departments
    ON employees.departmentId = departments.id
GROUP BY department, age_group
ORDER BY department, age_group;

INSERT INTO employees('name', 'salary', 'age', 'departmentId')
VALUES
    ('이성준', 20000, 28, 2),
    ('이성준2', 25000, 28, 3),
    ('이성준3', 10000, 28, 4),
    ('이성준4', 30000, 28, 1)

SELECT
    departments.name AS department,
    AVG(employees.salary) AS avg_salary_excluding_highest
FROM
    employees
INNER JOIN departments
    ON departments.id = employees.departmentId
WHERE salary < (
    SELECT MAX(employees.salary) 
    FROM employees
)
GROUP BY departments.id;