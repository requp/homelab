## Practical skills day 5
## iptables
#### Show all rules
```bash
`iptables -L` # for a pretty table
`iptables -L --line-number` # for the same table but with numbered rules
`iptables -S` # view as commands would be added manually 
```

#### Main options and rule specifications
- -t \<table-name> : filter, nat, mangle, raw or security (filter by default)
- -I \<CHAIN-NAME> - (add the chain rule to the first place) <br/>
Default chains are INPUT (for packets which go to the server), OUTPUT (out the server), FORWARD (the server is the intermediary) <br/>
- -A \<CHAIN-NAME> - append (add the rule to the bottom of the chain)
- -P \<CHAIN-NAME> - edit profile rule (for all packets which don't belong to any written rule)
- -s \<some-ip>/\<some-mask> - ipv4 source (singular ip with /32 mask or some custom subnet by mask)
- -d \<some-ip>/\<some-mask> - ipv4 destination (the same mask rule)
- -i \<input-interface-name> - input interfaces as wlan*, enp*, eth* etc
- -o \<output-interface-name> - output interfaces as wlan*, enp*, eth* etc
- -p \<protocol-name> - for example, for tcp or udp protocols
- --dport \<port-num> - destination port
- --sport \<port-num> - source port
- -j \<TARGET-NAME> - (ACCEPT, REJECT, DROP) targets option
#### Main targets
ACCEPT - allow packets with the given rule <br/>
REJECT - notify the source socket that the packet is rejected <br/>
DROP - just drop packets like they didn't exist
#### Save rules
```bash
iptables-save
```
Or download netfilter-persistent and use 
```bash
netfilter-persistent save
```
#### Save rules to file
```bash
iptables-save > /path/to/dir/rules.v4
```
#### Restore rules from file
```bash
iptables-restore < /path/to/dir/rules.v4
```
#### Replace a specific rule
`iptables -R <CHAIN-NAME> <rule-num> <new> <rule> <specification> <target>`
#### Delete a specific rule
`iptables -D <CHAIN-NAME> <rule-num>`
#### Drop all iptable rules
```bash
iptables -F
```

