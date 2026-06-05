## Prarctical skils of net programs
### ss
#### Most common ss command with options
`ss -tulpn` <br>
- -t - TCP sockets
- -u - UDP sockets
- -l - Sockets which are listenning rn
- -p - Show procceseses
- -n - Show numeric info (for example 22 instead of ssh)
#### Show all sockets
`ss -a`
#### Show additional columns with user info
`ss -e`
#### Show internal info
`ss -i`
#### Show only ip4 or ip6 sockets
`ss -4` or `ss -6`
#### Show summary statisctic
`ss -s`

### curl
#### Download a file and name it
`curl -o new_name.zip ftp://some/path/file.zip`
#### Download a file with the original name
`curl -O ftp://some/path/file.zip`
#### Show headers in response
`curl -i http://some/site`
#### Show raw data 
For examle a raw html page <br>
`curl http://some/site/index.html`
#### Fetch several sites or pages
Works with regex syntax <br>
`curl http://some/{site1, site2, site3/` or `curl http://some/site/page[1-8]` etc
#### Send data in a html form with POST method
`curl -d 'key1=value1&key2=value2' http://some/site`
#### Specify methods for http request (usefull for working/testing REST API)
`curl -X <METHOD-NAME> http://some/path
#### Upload files
`curl -T file-name ftp://some/path`
