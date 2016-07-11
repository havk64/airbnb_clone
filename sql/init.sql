/* ===------------------------------------------------------------------------===
 *      Startup script for Task 1
 *      Creating two MySQL isolated platforms
 *
 *      by Alexandro de Oliveira, for Holberton School.
 * ===-----------------------------------------------------------------------===
 */

-- Creating new users:
CREATE USER 'airbnb_user_dev'@'%'               IDENTIFIED BY 'yXBb*Xj?W83EeXX'; -- anywhere
CREATE USER 'airbnb_user_prod'@'localhost'      IDENTIFIED BY 'yXBb*Xj?W83EeXX'; -- localhost

-- Creating databases:
CREATE DATABASE airbnb_dev  CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE DATABASE airbnb_prod CHARACTER SET utf8 COLLATE utf8_general_ci;

-- Granting permissions:
GRANT ALL PRIVILEGES ON airbnb_dev.*  TO 'airbnb_user_dev'@'%';
GRANT ALL PRIVILEGES ON airbnb_prod.* TO 'airbnb_user_prod'@'localhost' ;
FLUSH PRIVILEGES;
