## sed
#### Show a whole file where with only first changed entry of each lines
`sed 's/<regex-target>/<change>/' filename` 
#### Show a whole file with only the first changed entry of each line
`sed 's/<regex-target>/<change>/g' filename`
#### Save data with changed entries in a new file
`sed 's/.../.../' <source-file >new-file`
#### Replace changed entries in the current file
`sed -i 's/.../.../' filename`
#### Delete specific entries
`sed -i '/<regex>/d' filename`
