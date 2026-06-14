# Practical skills for day 3
### Ansible file structure
#### inventory.ini
The file contain ips/hosts. It can be seperated by groups like:
```
[web_servers]
host1 some_variable=text
host2

[db_servers]
host3
host4
``` 

#### ansible.cfg
The file contain config setting for ansible like:
```
[defaults]
inventory=inventory.ini # Declare a file for inventory hosts
private_key=~/.ssh/ansible # Set up default path to find an ssh key for more secure (and more comfortable in some cases) connection
```

#### ansible instructions can be run from cli
```
ansible web_servers -i inventory -m ping
```

#### creating playbook for complex instructions
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
      when: ansible_distribution in ["Ubuntu", "Debian", "CentOS", "AlmaLinux"] # Condition to run this play only when the distridubiton matches list ones
      register: copy_file

    - name: install unzip # Name of the play
      tags: alma,debian,ubuntu,centos,unzip # Tags to specify plays to run from cli '-t' option 
      package: # Or any other ansible module
        name: unzip # Or any other package to install
        state: latest
        update_cache: yes # update packages for dnf/apt package manager
      when: copy_file.changed
      register: unzip_installed # register play to add dependency from this play to others

    - name: unarchive a file
      tags: alma,debian,ubuntu,centos,unzip
      unarchive:
        src: /path/to/dir/for/all/target/hosts/file.zip
        dest: /path/in/specific/host
        remote_src: yes
      when: unzip_installed.changed # Run only when the play above (with uzip registry) is executed
```
