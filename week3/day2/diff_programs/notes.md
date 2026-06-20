# Practical skills for day 2
## du
### Show a summary of the given dir path
`du -hs / # Will show s whole size of root dir`
### Show a summary of all sub dirs (including the given path) with the given depth
`du -h --max-depth=1 /`
### Show the top heaviest dir excluding empty ones
`sudo du -d 1 / 2> /dev/zero | sort -rn | awk '$1>0 {print $0}'`

## tmux
### Split the current window vertically
`ctrl + b` and `%`

### Split the current window horizontally
`ctrl + b` and `"`

### Move accros splited parts of the window
`ctrl + b` and: `up` or `down` or `left` or `right`

### Create a new window
`ctrl + b` and `c`

### Move between windows
`ctrl + b` and  from `0` to `9`

### Rename the current window
`ctrl + b` and `,`