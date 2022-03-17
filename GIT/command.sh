# This command sets the author name and email address respectively to be used with your commits
git config –global user.name "name"  
git config –global user.email "email address"

# This command is used to start a new repository
git init repository_name

# This command is used to obtain a repository from an existing URL.
git clone url_name

# This command adds a file to the staging area.
git add filename

# This command adds one or more to the staging area.
git add *

# This command records or snapshots the file permanently in the version history.
git commit -m "message"
git commit -m "message" filename

# This command commits any files you’ve added with the git add command and also commits any files you’ve changed since then.
git commit -a

# This command shows the file differences which are not yet staged.
git diff
git diff filename

# This command shows the differences between the two branches mentioned.
git diff first_branch second_branch

# This command shows the differences between the files in the staging area and the latest version present.
git diff –staged


