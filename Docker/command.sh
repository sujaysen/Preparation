# Get docker version
docker --version
# Docker information
sudo docker info
# Run docker image
sudo docker run image_name
# show all docker images
sudo docker images
# Remove docker images
docker rmi ImageID
# list all of the containers
sudo docker ps
# create a docker container
docker run -it ubuntu
#Any changes you make inside the container only apply to that container.
To exit the container, type exit at the prompt.
# see the top processes within a container
sudo docker top container_id
# Stop running container
sudo docker stop container_id
# delete a container
sudo docker rm container_id
# statistics of a running container.
sudo docker stats container_id
# pause the processes in a running container.
sudo docker pause container_id
sudo docker unpause container_id
# kill the processes in a running container.
sudo docker kill container_id
# start the Docker daemon process
sudo service docker start 
# stop the Docker daemon process
sudo service docker stop 
# docker build
sudo docker build  -t ImageName:TagName directory_name

