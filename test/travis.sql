# Create Testuser
CREATE USER 'dev'@'localhost';
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP ON *.* TO 'dev'@'localhost';
# Create DB
CREATE DATABASE IF NOT EXISTS `CLAS12OCR`;