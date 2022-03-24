# Installation on Ubuntu
# Check if Linux kernel version 3.8 and higher.
uname -a
# update the OS with the latest packages
sudo apt update
# add certificates
sudo apt install apt-transport-https ca-certificates curl software-properties-common
# add the GPG key 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# Add the Docker repository to APT sources
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
# install docker
sudo apt install docker-ce
# Check that it’s running
sudo systemctl status docker

