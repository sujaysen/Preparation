# Quit editor without saving changes
:q!
# Save changes and quit editor
:wq
ZZ
# Insert after cursor
i
# Insert text at the beginning of line
I
# Append after cursor
a
# Append text at the end of line
A
# Open new line below cursor
o
# Open new line above cursor
O
# Delete char and insert 
s
# set indentation 
open the file ~/.vimrc and the add following lines
set tabstop=4
syntax on " Syntax highlighting
set showmatch " Shows matching brackets
set ruler " Always shows location in file (line#)
set smarttab " Autotabs for certain code
set shiftwidth=4
set autoindent

# Set number into git add following line also
set number

# Vertically split
:vsp file_name

# Horizontally split
:sp file_name
# delete word from cursor position
dw
# Cut the current line
dd
# undo
u
# redo
Ctrl + r
# Paste the selected text before cursor
P
# Paste the selected text after cursor
p
# Copy the current line
yy
# Cut to EOL
D
# COPY TO EOL
y$
# Lowercase the entire line
Vu
# Upercase the entire line
VU
# Move the cursor to EOF
G
# Move the cursor to the beginning of the file
gg
# Saves lines 1 to 10 in myfile
:1,10 w file_name
# Appends lines 1 to 10 to myfile
:1,10 w >> file_name
# Inserts the content of myfile to current file
:r file_name
# Inserts the content of myfile under line 23
:23r file_name
# search forword direction
/<expression>
# search backword direction
?<expression>
# fold code
zc
# open from fold
zo
# close all folds
zM
# unfold all
zR
# match braces
%
# Accessing remote files
vim scp://user@server.com/filepath
# unindent to indent code 
=%
# differences between files
vimdiff <file> <file>
