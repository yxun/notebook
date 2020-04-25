

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

```
# vim tutorial
insert mode : i
nomal model: esc
basic movement h,j,k,l
navigate text: w,b,e
can combine with numbers
find and move to the next or previous occurrence of a character: f or F
jump to matching parenthesis : %
to the beginning of a line: 0
to the end of a line: $
find the next occurrence of the word under cursor: *
find the previous with : #
to the beginning of the file: gg
the end of the file: G
jump a specific line:2G (go to line 2)
search text: /text
repeat search:n,N
possible to use regexps
insert text into a new line:o,O (after new line is created, vim is set to insert mode)
delete the character:x,X
replace : r
delete command: d
repeat the previous command: .
visual mode: v (move and then what to do)
save: :w
quit: :q
quit without save: :q!
undo: u
redo: ctrl+R
help: :help
```

```
# set tab 2 space
:set ts=2

# set tab aligment line
:set listchars=tab:\|\ 
:set list
# note: there is a space after the last \ above

# show line number
:set number

# color scheme
syntax on
colorscheme murphy

# keep cursor in the middle of screen when editting
:imap <CR> <ESC>zzo

```