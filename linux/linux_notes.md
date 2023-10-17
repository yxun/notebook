
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



### File system

The following terms are encountered in describing file system directory contents:

- static is content that remains unchanged until explicitly edited or reconfigured.
- dynamic or variable is content typically modified or appended by active processes.
- persistent is content, particularly configuration settings, that remain after a reboot.
- runtime is process- or system-specific content or attributes cleared during reboot.

### Important file directories

- /usr  Installed software, shared libraries, include files, and static read-only program
data. Important subdirectories include:
  - /usr/bin        User commands.
  - /usr/sbin       System administration commands.
  - /usr/local      Locally customized software.

- /etc  Configuration files specific to this system.
- /var  Variable data specific to this system that should persist between boots. Files that dynamically change (e.g. databases, cache directories, log files, printer-spooled documents, and website content) may be found under /var.
- /run  Runtime data for processes started since the last boot. This includes process ID files and lock files, among other things. The contents of this directory are recreated on reboot. (This directory consolidates /var/run and /var/lock from older versions of Red Hat Enterprise Linux.)
- /home     Home directories where regular users store their personal data and configuration files.
- /root     Home directory for the administrative superuser, root.
- /tmp      A world-writable space for temporary files. Files which have not been accessed, changed, or modified for 10 days are deleted from this directory automatically. Another temporary directory exists, /var/tmp, in which files that have not been accessed, changed, or modified in more than 30 days are deleted automatically.
- /boot     Files needed in order to start the boot process.
- /dev      Contains special device files which are used by the system to access hardware.

Ref: hier(7) man page


### File globbing
```
Pattern Matches
* Any string of zero or more characters.
? Any single character.
~ The current user's home directory.
~username User username's home directory.
~+ The current working directory.
~- The previous working directory.
[abc...] Any one character in the enclosed class.
[!abc...] Any one character not in the enclosed class.
[^abc...] Any one character not in the enclosed class.
[[:alpha:]] Any alphabetic character.
[[:lower:]] Any lower-case character.
[[:upper:]] Any upper-case character.
[[:alnum:]] Any alphabetic character or digit.
[[:punct:]] Any printable character not a space or alphanumeric.
[[:digit:]] Any digit, 0-9.
[[:space:]] Any one whitespace character; may include tabs, newline, or carriage returns, and form feeds as well as space.
Note pre-set POSIX character class; adjusts for current locale.
```

### Conditional processing symbols

- & [...]  command1 & command2
  Use to separate multiple commands on one command line. Cmd.exe runs the first command, and then the second command.

- && [...]  command1 && command2
  
  Use to run the command following && only if the command preceding the symbol is successful. Cmd.exe runs the first command, and then runs the second command only if the first command completed successfully.

- || [...]  command1 || command2

  Use to run the command following || only if the command preceding || fails. Cmd.exe runs the first command, and then runs the second command only if the first command did not complete successfully (receives an error code greater than zero).

- ( ) [...]  (command1 & command2)

  Use to group or nest multiple commands.

- ; or , command1 parameter1;parameter2

  Use to separate command parameters.

### Linux Boot process

Power ON --> BIOS --> Master Boot Record (MBR) also known as First Sector of the Hard Disk
--> Boot Loader (e.g. GRUB) --> Kernel (Linux OS) --> Initial RAM disk - initramfs image
--> /sbin/init (parent process) --> Command Shell using getty --> X Windows System (GUI)

1) BIOS - The First Step
Power On --> BIOS (Basic Input/Output system) --> Initializes the screen and keyboard and tests the main memory

This process is also called POST (Power On Self Test). The BIOS software is stored on a ROM chip on the motherboard. After this, the remindeer of the boot process is completely controlled by the operating system.

2) Master Boot Records (MBR) and Boot Loader
Once the POST is completed, the system control passes from the BIOS to the boot loader. The boot loader is usually stored on one of the hard disks in the system, either in the boot sector. Up to this stage, the machine does not access any mass storage media.
Thereafter, information on the date, time, and the most important peripherals are loaded from the CMOS values (after a technology used for the battery-powered memory store - which allows the system to keep track of the date and time even when it is powered off).

The most common boot loaders for Linux are GRUB (GRand Unified Boot loader) and ISOLINUX (for booting from removable media). When booting Linux, the boot loader is responsible for loading the kernel image and the initial RAM disk into memory.

The boot loader has two stages:
First stage: For systems using the BIOS/MBR method, the boot loader resides at the first sector of the hard disk (MBR). The size of the MBR is just 512 bytes. In this stage, the boot loader examines the partition table and finds a bootable partition. Once it finds a bootable parition, it then searches for the second stage bootloader e.g. GRUB, and loads it into RAM

Second Stage: The second stage boot loader resides under /boot  A splash screen is displayed which allows us to choose which OS to boot. After choosing the OS, the boot loader loads the kernel into RAM. Kernels are almost always compressed, so it's first job is to uncompress itself.

The boot loader loads both the kernel and an initial RAM-based filesystem (initramfs) into memory.

The initramfs contains programs and binary files :
- mount proper root filesystem
- providing kernel functionality
- locating devices
- locating drivers and load them
- checking for errors in root filesystem

The mount program instructs the operating system that a file system is ready for use, and associates it with a mount point. If this is successful, the initramfs is cleared from RAM and the /sbin/init is executed.


### Interrupt

An interrupt is a signal to the processor emitted by hardware or software indicating an event that needs immediate attention. An interrupt alerts the processor to a high-priority condition requiring the interruption of the current code the processor is executing.


### Thrashing
Thrashing usually refers to a phenomena in memory and storage. It occurs when OS spends most of time on handing page faults (paging in or paging out). For example:
1. process A has some pages in hard drive and gets a page fault
2. The missing page (not in memory) needs to be swapped into memory
3. Suppose the memory is full, pages belong to process B need to be swapped out
4. Then process B needs to run, so its pages need to be swapped in and the process A's pages that were just swapped in need to be swapped out
5. This could happen indefinitely until the issue is resolved or one of the process finishes its job.

thrashing occurs when a computer's virtual memory subsystem is in a constant state of paging, rapidly exchanging data in memory for data on disk, to the exclusion of most application level processing.


### Thread vs Process
A process is a program in execution with an associated context, address space, and thread of execution (stacks pointer, registers, program counter). A process can also have multiple threads. Threads can be viewed as processes with the key difference that they share the same address space.

### Kernel
Kernel is a program running at all times on the computer. Typically, it is responsible for memory management, process management and disk storage management.

### fork
fork() causes creation of a new process. The new process (child process) is an exact copy of the calling process (parent process) except for process ID, parent process ID, descriptors, resource utilization

Initially both parent and child share the page(logically and physically) as long as they don't write to the page, when one of the processes attempts to write something to the page, then an extra copy of the page will be allocated. (copy-on-write)

### Difference between forking and multithreading
A fork gives us a brand new process which is a copy of the current process with the same code segment. It looks exactly like the parent process with different process id having it's own memory. Parent process creates a separate address space for the child with same code segments but executes independently of each other.
While threads can execute in parallel with same context. Also, memory and other resources shared between the threads causing less overhead. A thread process is considered a sibling while a forked process is considered a child. For all threads of any processes, communication between them is direct. While process needs some interprocess communication mechanism to talk to other processes.


### CPU burst, I/O burst
CPU burst is when the process is being executed in the CPU.
I/O burst is when the CPU is waiting for I/O for further execution. After I/O burst, the process goes into the ready queue for the next CPU burst

### preemptive and non-preemptive scheduling
preemptive scheduling: At times it is necessary to run a certain task that has a higher priority before another task although it is running. Therefore, the running task is interrupted for some time and resumed later when the priority task has finished its execution. 
e.g. Round Robin
non-preemptive scheduling: a running task is executed till completion. It cannot be interrupted.
e.g. FCFS

### short-term scheduler, long-term scheduler
Short-term scheduler also known as CPU scheduler descides which of the ready, in-memory processes is to be executed (allocated a CPU) after a clock interrupt, an I/O interrupt, an operating system call or another form of signal.
Long-term scheduler is also called a job scheduler. It determines which programs are admitted to the system for processing. It selects processes from the queue and loads them into memory for execution.

### Brief introduction to the Operating System Scheduling algorithms
1. First-Come, First-Served Scheduling
just a FIFO queue
2. Shortest-Job-First Scheduling (optimal)
pick the quickest fastest little job that needs to be done, get it out of the way first, and then pick the next smallest fastest job to do next. Uses the inverse of the next expected burst time as its priority.
3. Priority Scheduling
each job is assigned a priority and the job with the highest priority gets scheduled first
4. Round Robin Scheduling
similar to FCFS scheduling, except that CPU bursts are assigned with limits called time quantum. When a process is given the CPU, a timer is set for whatever value has been set for a time quantum.
a. If the process finishes its burst before the time quantum timer expires, then it is swapped out of the CPU just like the normal FCFS algorithm
b. If the timer goes off first, then the process is swapped out of the CPU and moved to the back end of the ready queue.

### How do you avoid SQL deadlock
1. Access objects in the same order
2. Avoid user interaction in transactions
3. Keep transactions short and in one batch
4. Use a lower isolation level
5. Use a row versioning-based isolation level
6. Use bound connections

### What is priority inversion ? how to fix it?
Shared resource needed by high priority processes are held by low priority processes, while low priority processes fail to get CPU usage. This makes the priority inversed (High priority waits for low priority.), and results in the situation that neither high priority process cannot execute normally (without resources) nor low priority cannot execute normally (without CPU)
solution: use "Priority Inheritance" to solve this situation. First, we allow low priority processes to inherit the priority of high priority processes, which makes low priority processes execute normally and exit and then release the resources. Thus, high priority process can get the resources they need and execute successfully.

### What is virtual memory?
virtual memory is a way of using hard drive to provide a memory for the computer. Elements of virtual memory are called pages. When a needed memory that is not in the real memory is requested a memory from virtual memory moves to real memory address.


### zombie processes & prevention
A zombine process or defunct process is a process that has completed execution (via the `exit` system call) but still has an entry in the process table; it is a process in the "Terminated state". This occurs for child processes, where the entry is still needed to allow the parent process to read its child's exit status: once the exit status is read via the `wait` system call, the zombie's entry is removed from the process table and it is said to be "reaped". A child process always first becomes a zombie before being removed from the resource table. In most cases, under normal system operation zombies are immediately waited on by their parent and then reaped by the system - processes that stay zombies for a long time are generally an error and cause a resource leak.

the `kill` command has no effect on a zombie process

an orphan process is a process that is still executing, but whose parent has died. These do not remain as zombie processes;

when a process is created in UNIX using fork() system call, the address space of the Parent process is replicated. If the parent process calls wait() system call, then the execution of parent is suspended until the child is terminated. At the termination of the child, a 'SIGCHLD' signal is generated which is delivered to the parent by the kernel. Parent, on receipt of 'SIGCHLD' reaps the status of the child from the process table. Even though, the child is terminated, there is an entry in the process table corresponding to the child where the status is stored. When parent collects the status, this entry is deleted. Thus, all the traces of the child process are removed from the system. If the parent decides not to wait for the child's termination and it executes its subsequent task, then at the termination of the child, the exit status is not read. Hence, there remains an entry in the process table even after the termination of the child. This state of the child process is known as the Zombie state.

different ways to prevent Zombie:
1. Using wait() system call
2. By ignoring the SIGCHILD signal
3. By using a signal handler


### deadlock
Deadlock is a situation when two or more processes wait for each other to finish and none of them ever finish.

The necessary conditions for deadlock:
* Mutual Exclusion: There is a resource that cannot be shared
* Hold and Wait: A process is holding at least one resource and waiting for another resource which is with some other process
* No Preemption: The operating system is not allowed to take a resource back from a process until processes gives it back
* Circular Wait: A set of processes are waiting for each other in circular form.

### POSIX
It is a family of standards specified by IEEE for maintaining compatibility between operating systems. POSIX defines the API, along with command line shells and utility interfaces, for software compatibility with variants of Unix and other operating systems.

### File descriptor
In Unix and related computer operating system, a file descriptor (FD) is an abstract indicator (handle) used to access a file or ther input/output resource, such as a pipe or network socket. File descriptors form part of the POSIX application programming interface. A file descriptor is a non-negative integer, generally represented in the C programming lanaguage as the type int (negative values being reserved to indicate "no value" or an error condition).

Each Unix process (except perhaps a daemon) should expect to have three standard POSIX file descriptors, corresponding to the three standard streams.
0   stdin
1   stdout
2   stderr

### Elaborate what happens under the hood after typing 'ls'
1. First of all, whenever we press a key on keyboard, the keyboard controller will emit an interrupt to processor(CPU) indicating there is an event that needs immediate attention. As interrupts ususally have high priority, the processor will suspending its current execution, save its state, and call an interrupt handler. Suppose we type 'l' then this character will be written the file that fd stdout points to, while shell's stdout usually points to screen, then 'l' will be shown on the screen. After the interrupt handler finishes its job, the process will resume its original work.
2. We type 'ls' and hit enter, then shell will first check out $PATH environment variable to see if there is a program 'ls' under each given path. Suppose we find /usr/bin/ls. Shell will call fork(), followed by execve("/usr/bin/ls"). fork() will create an identical child process and return twice. In parent(shell), it will typically call wait() to wait child process to complete. In child, it will execute execve() and a successful execve() will replace original data in the child process's address space with new data in order to run the new executable. Note that the file descriptors opened by parent will be kept.
3. Then the child process will be one that runs "/usr/bin/ls" code, it will make system calls(open(2), printf(3c) etc) to list directory entries in the current working directory. After the child process finishes its job, it will call exit()(usually called implicitly by 'return' in main()). Then all of the fds, streams will be closed. The parent process(in this case the shell) will be notified of child's termination, so wait() will be return and child exit code could be read from wait(). Then parent process can proceed.

* What will happen if another interrupt is received while the processor is running interrupt handler code ?
A: Different OS may have different ways to deal with this situation. For Linux, task of an interrupt handler is split into two halves, top half and botton half. Top half runs with interrupts disabled and respond to the interrupt as fast as possible, then botton half runs with interrupts enabled for as long as it needs and could be preempted.

* What do we call a child process when it terminates but its status has not been read by its parent with calls wait()?
A: Zombie process

* what is value of fd (in most case) will be returned by open() calling in the child process("/usr/bin/ls")?
A: 3, because stdin, stdout, stderr, will be 0,1,2 respectively, and lowest available fd will be returned.

* How is parent process notified when its children terminate?
A: SIGCHLD will be sent to the parent process

* How does shell implement I/O redirection if we want to redirect output of ls to another command as its input? like "ls | sort"
A: Briefly speaking, shell will call a pipe() before fork() to get two fds, rfd for read and wfd for write end, then call dup2(wfd,1) in ls and dup2(rfd,0) in sort.


### Paging vs Segmentation

Paging                                                  Segmentation
A page is a physical unit of information                A segment is a logical unit of information
A page is invisible to the user's program               A segment is visible to the user's program
A page is of fixed size e.g. 4K bytes                   A segment is of varying size
The page size is determined                             A segment size is determined by the user
by the machine architecture.
Fragmentation may occur                                 Segmentation eliminates fragmentation
Page frames on main memory are required                 No frames are required

### Fragmentation
In computer storage, fragmentation is a phenomenon in which storage space is used inefficiently, reducing capacity or performance and often both.

Internal fragmentation
Due to the rules governing memory allocation, more computer memory is sometimes allocated than is needed. The unusable memory is contained within an allocated region. This arrangement, termed fixed partitions, suffers from inefficient memory use - any process, no matter how small, occupies an entire partition.

External fragmentation
external fragmentation arises when free memory is separated into small blocks and is interspersed by allocated memory. It is a weakness of certain storage allocation algorithms. The result is that, although free storage is available, it is effectively unusable because it is divided into pieces that are too small individually to satisfy the demands of the application. The term "external" referes to the fact that the unusable storage is outside the allocated regions.

Data fragmentation
data fragmentation occurs when a collection of data in memory is broken up into many pieces that are not close together. It is typically the result of attempting to insert a large object into storage that has already suffered external fragmentation.

### Belady's Anomaly
also called FIFO anomaly. Usually, on increasing the number of frames allocated to a process virtual memory, the process execution is faster, because fewer page faults occur. Sometimes, the reverse happens, i.e., the execution time increases even when more frames are allocated to the process.

### Translation Lookaside Buffer (TLB)
In a cached system, the base addresses of the last few referenced pages is maintained in registers called the TLB that aids in faster lookup. TLB contains those page-table entries that have been most recently used.

