-- Write a SQL query to show only even rows from a table Employee.
Select * from Employee where mod(id,2)=0;

-- Write a SQL query to show only odd rows from a table Employee.
SELECT * FROM Employee WHERE mod(id,2)=1;