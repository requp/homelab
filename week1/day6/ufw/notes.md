## Practical skills for day 6
### ufw
#### Enable and disable rules
`ufw enable/disable`
#### Show all current rules
`ufw status numeric` - numeric for numbered rules
#### Change default profily rule
`ufw default allow/deny/reject <direction>` (incoming, outgoing, routed)
#### Main rule options
- in any port <port-num> - add a rule for a destination port (could be several with commas)
- from <ip>/<mask> - add a rule with a source ip/subnet
- to <ip>/<mask> - add a rule with a destination ip/subnet
- in/out out on <interace-name> - add a rule for a source/destinantion interface
- proto <protocol-name> - add a rule for a protocol
- comment 'some comment' - add a comment for a rule
- limit <port>/<protocol>- limit an amount of tries to connect in (for example, limit ssh/tcp could help against brute force)

### Out topic
My opinion is I still prefer iptables over ufw. When you get used to the iptables syntax - it makes more sense than the ufw one
