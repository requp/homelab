# Practical skills for day 3
## Ansible files' structure
### inventory.ini
The file contains IPs. It can be separated by groups like:
```
[web_servers]
host1 some_variable=text
host2

[db_servers]
host3
host4
``` 

### ansible.cfg
Ansible config file
```
[defaults]
inventory=inventory.ini # Declare a file for inventory hosts
private_key=~/.ssh/ansible # Set up default path to find an SSH key for a more secure (and more comfortable in some cases) connection
```

### Ansible instructions can be run from the CLI
```bash
ansible web_servers -i inventory -m ping
```

### Creating a playbook for more complex instructions
```yaml
---
- name name of the play
  hosts:
    - host_group1
    - host_group2
  become: yes
  tasks:
    - name copy archive
      tags: alma,debian,ubuntu,centos,unzip
      copy:
        src: /path/to/file/from/host/machine/file.zip
        dest: /path/to/dir/for/all/target/hosts/
      when: ansible_distribution in ["Ubuntu", "Debian", "CentOS", "AlmaLinux"] # Matches only given distribution names
      register: copy_file

    - name: install unzip # Name of the play
      tags: alma,debian,ubuntu,centos,unzip # Tags to specify plays to run from the CLI using the '-t' option 
      package: # Or any other Ansible module
        name: unzip # Or any other package to install
        state: latest
        update_cache: yes # update packages for dnf/apt package managers
      when: copy_file.changed
      register: unzip_installed # register a play to add a dependency from this play to others

    - name: unarchive a file
      tags: alma,debian,ubuntu,centos,unzip
      unarchive:
        src: /path/to/dir/for/all/target/hosts/file.zip
        dest: /path/in/specific/host
        remote_src: yes
      when: unzip_installed.changed # Run only when the play above (with the unzip registry) is executed
```
