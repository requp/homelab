# Basic commands in git

## Move between branches

### Create a new branch
`git switch -c <new_branch>`

### List branches
`git branch`

### Delete branch
`git branch -d (or -D for force) <branch_name>`


## Make commits
### Add all files or a specific file for a commit
`git add .` or `git add <some_path>/<some_file>`
### Make a commit with a comment
`git commit -m "Text for a comment"`

## Push branches
### Push a non-existed brach in a repository
`git push -u origin <branch_name>`
### Push changes in a existed branch
`git push origin <branch_name>` or `git push`

## Discard changes
### Delete changes in one file
`git checkout (HEAD for staged changes) <file>`

### Delete all changes
`git reset --hard`

### Stash all changes
`git stash`


