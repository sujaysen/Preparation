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
nsloopup # nslookup google.com
# get free space 
free -h
# command line calculator
bc
df
factor #  get all factor of a number
banner name 
sl
aafire
# You can use passwd command to change the password for self or any user
sudo passwd  -->> for self
passwd user_name  -->> for other user
# w is the short and simple command which will help you view the list of currently logged in users
w
# get current user
whoami
# Get history
history
# switch user or want to create new session
sudo login -->> for self
login user_name -->> for different user
# display all the CPU architecture information
lscpu
hostname
# Show current process tree
pstree
# get last loging user
last
# USB info
lsusb
shutdown
reboot
sort
uniq
wc
grep
ps -ef | grep systemd | grep -v grep
# login to remote server
ssh username@host
# transfers a URL
curl -X POST https://example.com/
# to pass parameter
curl -d "user=user1&pass=abcd" -X POST https://example.com/login
# to specify header
curl -d '{json}' -H 'Content-Type: application/json' https://example.com/login
# get json file in pretty format
cat filename | jq
# get size of a folder
du -sh folder_name
# See all open ports on your machine
netstat -anltp | grep "LISTEN"
# write
# Run a process with tag
nohup python3 app.py -m http.server 5050 &
# Run a process with another process name
nohup python3 app.py -a myProcess
ps -ef | grep "myProcess | awk `{print $2}`


