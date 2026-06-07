## awk
#### Show first column/field of the file
`awk '{print $1}' filename`
#### Show last column/field of the file
`awk '{print $NF}' filename`
#### Show a range of lines
`awk 'NR==2, NR==6 {print $0}' filename` # Or just NR==2 if only second line is needed
#### Change field separator
`awk -F'<new-character>' '{...}' filename`
#### Show only specific lines filtered by a regex expression
`awk '/<expression>/ {...}' filename'
