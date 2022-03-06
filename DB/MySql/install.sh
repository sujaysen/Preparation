# Installation
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
sudo mysql/ mysql -u root -p

# Create an user
CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
CREATE USER 'username'@'host' IDENTIFIED WITH mysql_native_password BY 'password';

# Update user
ALTER USER 'username'@'host' IDENTIFIED WITH mysql_native_password BY 'password';


# Grant privileges on db and table
GRANT PRIVILEGE ON database.table TO 'username'@'host';

# Particular privileges
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;

# ALL PRIVILEGES
GRANT ALL PRIVILEGES ON *.* TO 'username'@'host' WITH GRANT OPTION;

FLUSH PRIVILEGES;

# Testing MySQL
systemctl status mysql.service


