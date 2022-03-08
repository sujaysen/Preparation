# Write all command here
# SQL keywords are NOT case sensitive: select is the same as SELECT
 
# SELECT
SELECT column1, column2, ... FROM table_name;

# SELECT ALL
SELECT * FROM table_name;

# SELECT DISTINCT
SELECT DISTINCT column1, column2, ... FROM table_name;

# SELECT WHERE
SELECT column1, column2, ... FROM table_name WHERE condition;

# OPERATOR IN WHERE 
SELECT column1, column2, ... FROM table_name WHERE column = value;
SELECT column1, column2, ... FROM table_name WHERE column > value;
SELECT column1, column2, ... FROM table_name WHERE column >= value;
SELECT column1, column2, ... FROM table_name WHERE column < value;
SELECT column1, column2, ... FROM table_name WHERE column <= value;
SELECT column1, column2, ... FROM table_name WHERE column != value;
SELECT column1, column2, ... FROM table_name WHERE column BETWEEN value1 AND value2;
SELECT column1, column2, ... FROM table_name WHERE column NOT BETWEEN value1 AND value2;
SELECT column1, column2, ... FROM table_name WHERE column IN (value1,value2,...);
SELECT column1, column2, ... FROM table_name WHERE column NOT IN (value1,value2,...);
SELECT column1, column2, ... FROM table_name WHERE column LIKE 'pattern';

-->> 'a%'	Finds any values that start with "a"
-->> '%a'	Finds any values that end with "a"
-->> '%or%'	Finds any values that have "or" in any position
-->> '_r%'	Finds any values that have "r" in the second position
-->> 'a_%'	Finds any values that start with "a" and are at least 2 characters in length
-->> 'a__%'	Finds any values that start with "a" and are at least 3 characters in length
-->> 'a%o'	Finds any values that start with "a" and ends with "o"

# AND 
SELECT column1, column2, ... FROM table_name WHERE condition1 AND condition2 AND condition3 ...;

# OR
SELECT column1, column2, ... FROM table_name WHERE condition1 OR condition2 OR condition3 ...;

# NOT
SELECT column1, column2, ... FROM table_name WHERE NOT condition;

# ORDER BY
SELECT column1, column2, ... FROM table_name ORDER BY column1, column2, ... ASC|DESC;
-->> SELECT * FROM Customers ORDER BY Country ASC, CustomerName DESC;

# INSERT
INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);

# INSERT ALL COLUMN
INSERT INTO table_name VALUES (value1, value2, value3, ...);

# CHECK IS NULL
SELECT column_names FROM table_name WHERE column_name IS NULL;

# CHECK IS NOT NULL
SELECT column_names FROM table_name WHERE column_name IS NOT NULL;

# UPDATE
UPDATE table_name SET column1 = value1 , column2 = value2,... WHERE condition;
-->> UPDATE address SET pinCode = '111111' WHERE country = 'India'

# UPDATE ALL
UPDATE table_name SET column1 = value1 , column2 = value2,...

# DELETE
DELETE FROM table_name WHERE condition;

# DELEET ALL
DELETE FROM table_name;

# LIMIT
SELECT column_names FROM table_name WHERE condition LIMIT number;

# MIN
SELECT MIN(column_name) FROM table_name WHERE condition;

# MAX
SELECT MAX(column_name) FROM table_name WHERE condition;

# COUNT
SELECT COUNT(column_name) FROM table_name WHERE condition;

# AVG
SELECT AVG(column_name) FROM table_name WHERE condition;

# SUM
SELECT SUM(column_name) FROM table_name WHERE condition;

# ALIAS
SELECT column_name AS alias_name FROM table_name;


