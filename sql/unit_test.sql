
/* ===------------------------------------------------------------------------===
 *      Test script for Task 0, Project Unit Test - Airbnb Clone.
 *      Isolating configuration
 *
 *      by Alexandro de Oliveira, for Holberton School.
 * ===-----------------------------------------------------------------------===
 */

CREATE USER 'airbnb_user_test'@'%' IDENTIFIED BY 'unit_test_pass'; -- anywhere

CREATE DATABASE airbnb_test  CHARACTER SET utf8 COLLATE utf8_general_ci;

GRANT ALL PRIVILEGES ON airbnb_test.*  TO 'airbnb_user_test'@'%';
