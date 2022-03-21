# This command sets the author name and email address respectively to be used with your commits
git config –global user.name "name"  
git config –global user.email "email address"

# Store username and pass details into cachei with default time 15 min
git config --global credential.helper cache
git config credential.helper store

# This command is used to start a new repository
git init repository_name

# This command is used to obtain a repository from an existing URL.
git clone url_name

# This command adds a file to the staging area.
git add filename

# This command adds one or more to the staging area.
git add *
git add .

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

# This command unstages the file, but it preserves the file contents.
git reset filename

# This command lists all the files that have to be committed.
git status

# This command deletes the file from your working directory and stages the deletion.
git rm filename

# This command is used to get list of commits
git log

# This command is used to get list of commits of a particular file
git log --follow filename

# This command shows the metadata and content changes of the specified commit.
git show commit_id     # get commit id from git log also

# This command is used to give tags to the specified commit.
git tag commit_id

# This command lists all the local branches in the current repository.
git branch

# Create a branch
git branch branch_name

# Delete a branch
git branch -d branch_name

# This command is used to switch from one branch to another.
git checkout branch_name

# This command creates a new branch and also switches to it.
git checkout -b branch_name

# This command merges the specified branch’s history into the current branch.
git merge branch_name

# This command sends the committed changes of master branch to your remote repository.
git push origin master

# This command pushes all branches to your remote repository.
git push -all origin

# Pull from git
git pull

# Delete changes 
git stash

# This command temporarily stores all the modified tracked files.
git stash save

# This command restores the most recently stashed files.
git stash pop

# This command lists all stashed changesets.
git stash list

# This command discards the most recently stashed changeset.
git stash drop
