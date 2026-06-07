## Practical skills for day 6
## ufw
#### Enable and disable rules
`ufw enable/disable`
#### Show all current rules
```bash 
ufw status numeric # numeric for numbered rules
```
#### Change default profile rule
`ufw default allow/deny/reject <direction>` (incoming, outgoing, routed)
#### Main ufw rule options
- in any port \<port-num> - add a rule for a destination port (could be several with commas)
- from \<ip>/\<mask> - add a rule with a source ip/subnet
- to \<ip>/\<mask> - add a rule with a destination ip/subnet
- in/out out on \<interface-name> - add a rule for a source/destination interface
- proto \<protocol-name> - add a rule for a protocol
- comment 'some comment' - add a comment for a rule
- limit \<port>/\<protocol>- limit an amount of tries to connect (for example, limit ssh/tcp port-protocol could help against brute force)
___
## Out of topic
My opinion is I still prefer iptables over ufw. When you get used to the iptables syntax - it makes more sense than the ufw one
