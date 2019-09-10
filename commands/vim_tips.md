

```
# Question: Shell unexpected end of file error

You probably have invisible CR characters at the end of your lines (like when the file is in Microsoft format where the lines are terminated by the CRLF sequence of characters instead of just LF).
Then, the shell complains that it reaches the end of the script file without finding a then following the if (there's just a then<CR>).

issue a :set ff=unix in vim to fix your script file.


# Quesiton: How to solve "bad interpreter: No such file or directory"

Remove the ^M at the end of usr/bin/perl from the #! line at the beginning of the script. That is a spurious ASCII 13 character that is making the shell go crazy. Possibly you would need to inspect the file with a binary editor if you do not see the character.

You could do like this to convert the file to Mac line-ending format:
$ vi your_script.sh
:set ff=unix


```