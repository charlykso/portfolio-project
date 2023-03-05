CREATE DATABASE IF NOT EXISTS authentified_db;
CREATE USER IF NOT EXISTS 'authentified_user'@'localhost';
SET PASSWORD FOR 'authentified_user'@'localhost' = 'auth_pwd';
GRANT USAGE ON *.* TO 'authentified_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'authentified_user'@'localhost';
GRANT ALL PRIVILEGES ON `authentified_db`.* TO 'authentified_user'@'localhost';
FLUSH PRIVILEGES;

mysqldump -u [username] -p [database name] > [database name].sql
mysql -u [username] -p newdatabase < [database name].sql

AUTH_MYSQL_USER=authentified_user AUTH_MYSQL_PWD=auth_pwd AUTH_MYSQL_HOST=localhost AUTH_MYSQL_DB=authentified_db python3 -m web_dynamic.app
AUTH_MYSQL_USER=authentified_user AUTH_MYSQL_PWD=auth_pwd AUTH_MYSQL_HOST=localhost AUTH_MYSQL_DB=authentified_db python3 -m web_dynamic.app
