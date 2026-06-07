# Basic options in git

## 1. Move between branches

#### Create a new branch
`git switch -c <new_branch>`

#### List branches
```bash
git branch
``` 

#### Delete branch
`git branch -d (or -D for force) <branch_name>`


## 2. Make commits
#### Add all files or a specific file for a commit
`git add .` or `git add <some_path>/<some_file>`
#### Make a commit with a comment
```bash
git commit -m "Text for a comment"
``` 

## 3. Push branches
#### Push a non-existed branch in a repository
`git push -u origin <branch_name>`
#### Push changes in an existing branch
`git push origin <branch_name>` or `git push`

## 4. Discard changes
#### Delete changes in one file
`git checkout (HEAD for staged changes) <file>`

#### Delete all changes
```bash
git reset --hard
``` 

#### Stash all changes
```bash
git stash
``` 

