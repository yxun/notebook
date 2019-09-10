


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


```