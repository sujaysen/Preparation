# Change directory
cd path_directory
# Nevigate to parent directory
cd
# Show files and folders
ls
ls -l
ls -lrth
# concate files
cat file_name
# create a new file without any content
touch file_name
# Create new directory
mkdir directory_name
# Get current working directory
pwd
# Remove file
rm file_name
# remove directory
rm -r directory_name
# download application/web pages directly from web
wget url_name
# Rename file/directory
mv source_file dest_file
mv -r source_file dest_file
# Copy file/directory
cp source_file dest_file
cp -r source_file dest_file
# view like tree
tree
tree -f # show in current direcory
# head command
head file_name
# tail command
tail file_name
# wc Command
wc filename
# locate command
locate file_name
# copy from local to remote
scp file.txt remote_username@ip:/remote_directory/newfilename.txt
# Remote to local
scp remote_username@10.10.0.2:/remote/file.txt /local/directory
# remote to remote
scp user1@host1.com:/files/file.txt user2@host2.com:/files	
# show process
ps -ef |grep "name of application"
# kill process
kill -9 process_id
# detect whether a system is connected to the network or not
ping ip/domain
# display the IP address for a given domain name
host domain_name
# to see date
date
# to see calender
cal
# check ip
ifconfig


