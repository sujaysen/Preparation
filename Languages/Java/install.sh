# Installing the Default JRE/JDK
sudo apt update # update the packages
java -version # check version 
sudo apt install default-jre # install jre
sudo apt install default-jdk # install jdk

# managing java
# open the file /etc/environment
sudo vim /etc/environment
# put the line 
JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
# save and close the file
source /etc/environment

