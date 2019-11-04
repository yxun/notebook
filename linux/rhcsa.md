
### SSH
* How to generate a SSH key pair ?
* How to share the public key ?

```shell
# generate ssh key pair
$ ssh-keygen -b 2048 -t rsa -f .ssh/id.rsa -q -N "" -C "yuanlin.yxu@gmail.com"

# permission modes must be 600 on the private key and 644 on the public key

# share the public key
$ ssh-copy-id -I .ssh/id_rsa.pub user@remotehost
# enter user@remotehost login password

# use ssh-agent can store ssh key pair password

```

Ref:

* ssh-keygen(1)
* ssh-copy-id(1)
* ssh-agent(1)
* ssh-add(1)

### File Systems
* copy, move, create, delete, and organize files

* what are the important directories ?
* how to create hard link ?
* how to create soft link ?
* what's the difference between hard link and soft link ?

```shell
# /usr, /etc, /var, /run, /home, /root, /tmp, /boot, /dev
# cp, mv, mkdir, rm

# create hard link
$ ln [existing file] [hard link]

# find out whether two files are hard links of each other
$ ls -il
# all hard links that reference the same file will have the same link count, access permissions, user and group ownerships, time stamps, and file content

# data is only deleted from storage when the last hard link is deleted

# hard links can only be used with regular files
# hard links can only be used if both files are on the same file system
# use df, files in two different "Mounted on" directories and their subdirectories are on different file systems

# soft link is not a regular file, but a special type of file that points to  an existing file or directory
$ ln -s [existing file] [soft link]

# a soft link pointing to a missing file is called a "dangling soft link"

# A hard link points a name to data on a storage device
# A soft link points a name to another name, that points to data on a storage device

```

Ref:
* hier(7)
* ln(1)

### Users Groups
* create, manage, and delete local users and groups

* how to configure sudo ?
* how to access the root account ?
* how to create, modify, delete users ?
* how to solve "sudo: /etc/sudoers.d is world writable" ?
* how to create nologin user ?
* how to prevent user account password expired ?
* how to add a group for an user ?
* how to find all unowned files and directories ?
* how to set password for an user ?
* how to create, modify, delete a group ?
* how to check existing users and groups ?

```shell
# configure sudo
# /etc/sudoers or /etc/sudoers.d/user01
user01  ALL=(ALL)  NOPASSWD:ALL

# access the root account
$ sudo su -

# useradd, usermod, userdel

# Delete user
$ su - username
$ kill -9 -1
or 
$ lsof -u username
# kill the process
or 
$ pkill -u username
and then
$ userdel -r username

# Add user
$ useradd -m -g initial_group -G additional_groups -s login_shell username

# sudoers file permission
$ chmod 755 /etc/sudoers

# add nologin user
$ usermod -s /sbin/nologin user01

# disable password aging for an user account
$ chage -m 0 -M 99999 -l -1 -E -1 user01
$ chage --list user01
# force user to update its password on the next login
$ chage -d 0 user01

# edit default password aging configuration in the /etc/login.defs only be effective for new users only. 
# The existing users will continue to use the old password aging settings

# lock user and expire an account
$ usermod -L -e 2019-10-05 user01


# append group
$ usermod -aG group user
  
# find all unowned files and directories
$ find / -nouser -o -nogroup

# set password
$ passwd user01

# RHEL8 UID Ranges
UID 0 always assigned to root
UID 1-200 a range of "system users" assigned statically to system processes
UID 201-999 a range of "system users" assigned dynamically. runs as "unpriviledged" system users
UID 1000+ regular users
# RHEL 7 UID 1-499 system users, UID 500+ regular users
# default ranges used by useradd and groupadd can be changed in the /etc/login.defs

# create a group
$ groupadd -g GID group01
# system group GID 0-999
# -r creates a system group

# you cannot remove a group if it is the primary group of any existing user

# check existing users 
$ id user01
$ tail /etc/passwd
# check group
$ tail /etc/group

```

Ref:
* id(1), passwd(5), group(5)
* su(1), sudo(8), visudo(8), sudoers(5)
* useradd(8), usermod(8), userdel(8)
* group(5), groupadd(8), groupdel(8), usermod(8)
* chage(1), usermod(8), shadow(5), crypt(3)


### File Permission
* Set Linux file system permissions on files and to interpret the security effects of different permission settings

* how to change file permission ?
* how to change file ownership ?
* how to check permission code number ?
* what are the special permissions ?
* how to configure default file permissions ?

```shell
$ chmod WhoWhatWhich file|directory
# Who is u, g, o, a (user, group, other, all)
# What is +, -, = (add, remove, set exactly)
# Which is r, w, x (read, write, execute)


# check permission number
$ stat -c "%a %n" .

# chmod ### file|directory
# Each digit represents permissions for user, group, other
# The digit is calculated by adding together numbers, 4 for read, 2 for write, and 1 for execute

# special permissions
u+s (suid)   File executes as the user that owns the file, not the user that ran the file
g+s (sgid)   File executes as the group that owns the file
o+t (sticky)   Users with write access to the directory can only remove files that they own

Numerically (fourth preceding digit): setuid = 4, setgid = 2, sticky = 1

# Default file permissions
If a bit is set in the umask, then the corresponding permission is cleared on new files
# the system's default umask values are defined in the /etc/profile and /etc/bashrc 

```

Ref:
* ls(1), chmod(1), chown(1), chgrp(1)
* bash(1), ls(1), chmod(1), umask(1)

### SELinux
* how to display SELinux contexts ?
* how to change the current SELinux mode ?
* how to set the default SELinux mode ?
* how to change the SELinux context ?
* how to adjust SELinux booleans ?
* how to monitor SELinux violations ?

```shell
# SELinux labels have several contexts: user, role, type, and sensitivity

# display SELinux contexts: ps, ls, cp, mkdir   -Z or -Zd

# change SELinux mode
$ getenforce
$ setenforce [ Enforcing | Permissive | 1 | 0 ]

# set the default SELinux mode, /etc/selinux/config

# change the SELinux context, semanage, fcontext, restorecon, and chcon
# The preferred method, declare the default labeling
$ semanage fcontext [-a, -d, -l]
# and then applying that context to the file
$ restorecon -Rv filename

# example
$ semanage fcontext -a -t httpd_sys_content_t '/virtual(/.*)?'
$ restorecon -RFvv /virtual

# manage SELinux booleans
$ getsebool -a
$ sudo setsebool [-P policy] [on | off]
$ sudo semanage boolean -l
# -P writes all pending values to the policy, making them persistent


# SELinux log, install setroubleshoot-server package
$ sudo tail /var/log/audit/audit.log
$ sudo tail /var/log/messages
$ sealert -l 

# fix error
$ restorecon -R 
```

Ref:
* getenforce(1), setenforce(1), selinux_config(5)
* chcon(1), restorecon(8), semanage(8), semanage-fcontext(8)
* booleans(8), getsebool(8), setsebool(8), semanage(8), semanage-boolean(8)
* sealert(8)


