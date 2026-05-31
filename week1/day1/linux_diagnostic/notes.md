# Basic knowledge of programs find, journalctl, ssh-keygen/ssh-copy-id, htop

## htop

### Sort for proccessor or memory usage
P or M

### Search for command line
/

### Change nice 
F8

### Send a signal
F9

### Sort for choicen column
F6

## journalctl

### Filter by a service name
`journalctl -u nginx -u mysql` (could be several services in one output)

### Filter by time
`journalctl --since "year-month-day hour:min:sec"/"yesterday" etc/"2 hours ago" --until (the same posibillities)`

### Show first/last n strings
`journalctl -n +5 (first five)/5 (last five)`

### Show logs in RealLife
`journalctl -f`

### Filter by uid, guid or/and pid
`journalctl _UID=<id>/_GID=<id>/_PID=<id>`

### Filter by priority
From 0 to 7 or words (emerg, alert, crit, err, warning, notice, info, bebug)
`journalctl -p err`

### Filter by sessions splited by rebooting the system
From 0 to negative numbers or id of a specific session. Command `journactl --list-boots` can help
`journalctl -d -2`

### Represent output in other formats
Formats are: json, json-pretty (both gives more info in json format) , cut (only log message), export (raw binary output), verbose (more info about log) 
`journalctl -o <format_name>`

### Show only kernel logs
`journalctl -k`

### Show much space journalctl logs take
`journalctl --disk-usage`

### Limit journalctl logs by disk usage
`journalctl --vacuum-size=1G`

### Limit journalctl logs by time
`journalctl --vacuum-time=1years`

### Show logs in UTC, not your local machine time
`journalctl --utc`


## find

### Filter file/dir by case-sensitive(insensitive) name

`find /some/path -name "case-sensitive name"` or `find -iname "case-insensitive name"

### Add 'not' to any optinon
`find /some/path -not -name "some name"` - in this case any files/dirs but not with the given name 

### Combine several identical options with 'or'
`find /some/path -name "some name" -or -name "diff title"` - all files/dirs with these 2 given names

### Filter file/dir by type
Types are: f (file), d (dir), l (symb link), b (block device), c (character device)
`find /some/path -type f -name "*.log"`

### Filter by size
Sizes are: c, k, M, G, b (512-byte blocks). If use '-' less than the size, '+' bigger than the given size
`find /some/path -size 1G`

### Filter by access/modification/change time
modification is editing data in a file
change is meta data changing in inode
time in days, -days means last n days, +days means all files/dirs that are older than given days
min in mins
`find /some/path atime/mtime/ctime -7 -name "some name"`

### Find dir/files that are newer than given file
`find /some/path -newer given_file`

### Filter by user/group ownership
`find -user/-group user/group_name`

### Filter by permission
`find /some/path -perm <ugo> (exact permission)/-<ugo> (this perm or higher)`

### Filter by emptiness
`find /some/path -type d -empty`

### Execute other command to all output results
`find /some/path -user old_user -exec chown new_user {} \;`

## ssh-keygen, ssh-id-copy

### Make ssh keys
Make ssh key from your local machine
`ssh-keygen` maybe add password for additional security

### Copy a public ssh key to target server
`ssh-id-copy user@target-server`

