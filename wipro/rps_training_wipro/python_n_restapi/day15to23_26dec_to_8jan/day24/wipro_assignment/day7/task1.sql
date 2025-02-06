-- Task 1: Write SQL queries to create a table named 'Users' and insert multiple records into it.

-- Create table 'Users'
CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    age INT
);

-- Insert records into 'Users'
INSERT INTO Users (name, email, age) VALUES
('Manish1', 'manish1@rps.com', 25),
('Manish2', 'manish2rps.com', 30),
('Manish3', 'manish3@rps.com', 22);
