CREATE DATABASE IF NOT EXISTS `web_scraper_db`;
USE `web_scraper_db`;
CREATE TABLE IF NOT EXISTS `quotes`(
	id INT AUTO_INCREMENT PRIMARY KEY,
    quote_text TEXT NOT NULL,
    author VARCHAR(255) NOT NULL
);
ALTER TABLE `quotes` ADD CONSTRAINT unique_quote UNIQUE (quote_text(255), author);