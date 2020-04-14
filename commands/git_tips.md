


```shell
# revert changes made to your working copy
$ git checkout .

# reset all unpushed commits and revert changes made to the index
$ git reset

# revert a change that you have commited
$ git revert ...

# remove untracked files
$ git clean -f

# remove untracked directories
$ git clean -d

# using other ssh key for git
$ GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa_example" git clone example

# change remote url
$ git remote set-url origin your_repo_ssh_url

# config username and useremail
$ git config --global user.name "user1"
$ git config --global user.email "user1@example.com"

# git skip login username/password
$ git remote set-url origin git@github.com:<username>/<project>.git

# sync fork with upstream
$ git remote -v
$ git remote add upstream [upstream git repo]
$ git fetch upstream
$ git checkout master
$ git merge upstream/master
$ git push


# git how to rollback a rebase
$ git reflog

# find the first action before rebase
$ git reset HEAD@{}  --hard

# avoid git pull problems, git pull == git fetch; git merge
# create an alias git up
$ git config --global alias.up '!git remote update -p; git merge --ff-only @{u}'
$ git up
# This alias downloads all of the latest commits from all upstream branches
#  (pruning the dead branches) and
#  tries to fast-forward the local branch to the latest commit on the upstream branch

# avoid git pull, a better approach is e.g. git fetch; git rebase origin/master
# or git pull --rebase

# avoid fast-forward git merge, use git merge --no-ff to keep a history of a feature branch

```
