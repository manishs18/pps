-- Task 2: Write a SQL query to update a record in the 'Users' table and then delete a record from it.

-- Update record in 'Users'
UPDATE Users
SET age = 26
WHERE name = 'Manish';

-- Delete record from 'Users'
DELETE FROM Users
WHERE name = 'Mnaish2';
