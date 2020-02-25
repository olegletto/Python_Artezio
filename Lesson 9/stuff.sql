CREATE DATABASE IF NOT EXISTS staff;
USE staff;

CREATE TABLE IF NOT EXISTS managers (
id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
money INT
);

INSERT INTO managers (id, first_name, last_name, money) VALUES (NULL, 'Egor', 'Creed', 200000);
INSERT INTO managers (id, first_name, last_name, money) VALUES (NULL, 'Max', 'Korzh', 123000);
INSERT INTO managers (id, first_name, last_name, money) VALUES (NULL, 'Adam', 'Sandler', 234000);
INSERT INTO managers (id, first_name, last_name, money) VALUES (NULL, 'Chris', 'Brown', 25000);
INSERT INTO managers (id, first_name, last_name, money) VALUES (NULL, 'Rod', 'Stewart', 435765);

CREATE TABLE IF NOT EXISTS post (
id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
post_name VARCHAR(30) NOT NULL
);

INSERT INTO post (id, post_name) VALUES (NULL, 'BIG BOSS');
INSERT INTO post (id, post_name) VALUES (NULL, 'JUNIOR');
INSERT INTO post (id, post_name) VALUES (NULL, 'CLEANER');

ALTER TABLE managers ADD post_id INTEGER NOT NULL;

UPDATE managers SET post_id=1 WHERE id=5;
UPDATE managers SET post_id=2 WHERE id IN (1,2,3);
UPDATE managers SET post_id=3 WHERE id=4;

UPDATE managers SET money=20000  WHERE id=1;
UPDATE managers SET money=12300  WHERE id=2;
UPDATE managers SET money=23400  WHERE id=3;
UPDATE managers SET money=2500  WHERE id=4;

SELECT first_name, last_name FROM managers WHERE money < 30000;

SELECT first_name, last_name FROM managers WHERE post_id=2 AND money < 30000;


