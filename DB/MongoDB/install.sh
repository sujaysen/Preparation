# Import the public key used by the package management system.
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

# Create a list file for MongoDB.
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

# Reload local package database.
sudo apt-get update

# Install the MongoDB packages.
sudo apt-get install -y mongodb-org

# Start MongoDB.
sudo systemctl start mongod

# If Failed to start mongod.service: Unit mongod.service not found.
sudo systemctl daemon-reload

# Verify that MongoDB has started successfully.
sudo systemctl status mongod
sudo systemctl enable mongod

# Stop MongoDB.
sudo systemctl stop mongod

# Restart MongoDB.
sudo systemctl restart mongod

# Begin using MongoDB.
mongosh
