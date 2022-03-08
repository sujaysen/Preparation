# Uninstallation
# Stop MySQL service
sudo systemctl stop mysql

# Remove all package
sudo apt-get purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-*

# Remove MySQL configuration and data
sudo rm -rf /etc/mysql /var/lib/mysql

# Remove unnecessary packages.
sudo apt autoremove

# Remove apt cache.
sudo apt autoclean


