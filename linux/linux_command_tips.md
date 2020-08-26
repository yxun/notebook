
```shell

# date format example
$ date
Sat Apr 5 08:13:50 PDT 2014
$ date +%R
08:13
$ date +%x
04/05/2014
$ date +%r
10:14:07 AM

# find out largest directories and files
$ du -a /var | sort -n -r | head -n 10

# list journal disk usage
$ journalctl --disk-usage

# You can control the size of this directory using this parameter in your /etc/systemd/journald.conf:  SystemMaxUse=50M

# You can force a log rotation:
$ sudo systemctl kill --kill-who=main --signal=SIGUSR2 systemd-journald.service

# NOTE: You might need to restart the logging service to force a log rotation, if the above signaling method does not do it. You can restart the service like so:
$ sudo systemctl restart systemd-journald.service

# check kernel Version
$ uname -a

# Distribution info
$ lsb_release -a
$ cat /etc/lsb_release
$ cat /etc/issue.net
$ cat /etc/redhat-release

# extract tar.xz file
$ tar -xJf file.tar.xz

# extract tar.gz file
$ tar -vxzf file.tar.gz

# extract zip file
$ unzip file.zip -d destination_folder

# check process
$ ps aux

# check a process name from pid
$ ps -fp PID

# Delete user steps
$ su - <username>
$ kill -9 -1

# Exit the shell and try the userdel -r username again.
$ userdel -r <username>

# Or you can check for processes from the user using lsof -u username and kill the relevant PIDs.
$ lsof -u <username>

# Or pkill -u username or pkill -u uid
$ pkill -u <username>

# Bash script get the path where it stored in
`$ DIR="$(cd "$(dirname $0)" && pwd -P)"`

# list all existing user accounts
$ passwd -Sa

# list all local user accounts
$ cut -d: -f1 /etc/passwd | column

# add user
$ useradd -m -g <initial_group> -G <additional_groups> -s <login_shell> <username>

# change a user login name
$ usermod -l <newname> <oldname>
# change a user home directory
$ usermod -d </my/new/home> -m <username>

# How to solve “sudo: /etc/sudoers.d is world writable”
$ chmod 775 /etc/sudoers

# generate ssh key pair
$ ssh-keygen -b 2048 -t rsa -f <id.rsa file path> -q -N "" -C "<email address>"

# check permission code
$ stat -c "%a %n" .

# check selinux status
$ sestatus

# OpenSSL connect to SSL services
$ openssl s_client -connect https://example.com:443
$ opensll s_client -connect https://example.com:443 -CAfile /etc/ssl/certs/ca-certs.crt

# check port opening
$ nc -v [dest host] [port]

# check if port is in use in locally
$ sudo lsof -i -P -n | grep LISTEN
$ sudo netstat -tulpn | grep LISTEN
$ sudo lsof -i:22  ## see a specific port such as 22
$ sudo ss -tulw

# MacOS X
$ netstat -anp tcp | grep LISTEN
$ netstat -anp udp | grep LISTEN

# Windows
$ netstat -bano | grep LISTENING

# how to move all files except one
$ shopt -s extglob
$ mv !(fileone) <~/path/newFolder>

# how to lock a file
$ chattr +i file

# how to get the MAC address of the network interfaces
$ ip link
# or
$ ifconfig -a

# how to check product_uuid
$ sudo cat /sys/class/dmi/id/product_uuid

# how to view linux kernel parameters for currently booted system
$ sudo sysctl -a | grep 'something'
# or
$ cat /proc/cmdline
# or
$ dmesg | grep "command line"

# how to terminate dropped ssh sessions
$ pkill -o -u YOURUSERNAME sshd

# how to command for each file in a folder
$ for f in ./*.doc; do
    # do something with "$f"
done

# alternative to netstat -s
https://unix.stackexchange.com/questions/258711/alternative-to-netstat-s
e.g.
$ awk '{for(i=1;i<=NF;i++)title[i] = $i; getline; print title[1]; for(i=2;i<=NF;i++)printf " %s: %s\n", title[i], $i }' /proc/net/netstat | grep DelayedACKLost

# mount external USB disk drive

## check commands
## check device name
$ lsblk --fs
$ sudo fdisk -l
## check disk mount
$ df -h
## check dmesg log
$ dmesg | grep <device name>
## check mount
$ findmnt

## create directory
$ sudo mkdir /media/<directory name>
## mount disk
$ sudo mount -t <fs type, e.g. hfsplus> <device name, e.g. /dev/sda1> /media/<directory name>

## unmount
$ sudo umount /media/<directory name>

## eject device
$ sudo eject /dev/sda


# identify users who own a directory
$ df -h
$ id -a 42
# http://ngelinux.com/what-is-the-meaning-and-impact-of-run-user-0-and-run-user-1000-directories-in-linuxfedora/


```

