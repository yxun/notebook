

## File system

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


