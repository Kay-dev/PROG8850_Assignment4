CREATE DATABASE IF NOT EXISTS subscriptions;
USE subscriptions;

CREATE TABLE IF NOT EXISTS subscribers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(50) NOT NULL,
    `email` VARCHAR(255) NOT NULL
);