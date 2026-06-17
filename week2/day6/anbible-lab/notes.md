# Practical skills for day6
### 1. Handlers and template hiearchy

```
📁 some_dir/
│
├── 📄 playbook_with_role_names.yaml
├── 📁 host_vars/
│   ├── 📄 192.168.10.30
│   ├── 📄 some-host
│   └── 📄 ...
├── 📄 playbook_with_role_names.yaml
└── 📁 roles/
    │
    ├── 📁 role1/
    │   ├── 📁 tasks/
    │   │   └── 📄 main.yaml
    │   ├── 📁 files/
    │   │   ├── 📄 some_file
    │   ├── 📁 handlers/
    │   │   └── 📄 main.yml
    │   ├── 📁 templates/
    │   │   ├── 📄 template1.j2
    │   │   ├── 📄 template2.j2
    │   │   └── 📄 ...
    │
    ├── 📁 role2/
    │   ├── 📁 .../
    │   └── ...
    │
    └── 📁 ... (more roles)
```

### 2. Handlers structure
Handlers are just main.yaml file in `roles/role_name/` directory which contains independent tasks without declaring host and other options above <br/>
They can be triggered with a task in the role main file with statement `notify <handler_name>`
```yaml
# roles/docker_servers/tasks/main.yaml
...
  - name: Stop and enable docker 
    systemd:
      name: docker
      state: stopped
    notify: restart_docker # The exact name like in handlers file
...
```

```yaml
# roles/docker_servers/handlers/main.yaml
...
- name: restart_docker
  systemd:
    name: docker
    state: restarted
...
```

### 3. Templates structure
Templates are just a files with j2 format wich allow to add variables in the files and replaced them with target ones
```bash
# roles/base/templates/template1.j2
...
{{ some_var_name }}
...
```

```bash
# host_vars/192.168.10.30
# For ex. host_var dir for variables
...
some_template: template1.j2
...
```

```yaml
# roles/base/tasks/main.yaml
...
  - name: Change program_name config config
  tags: program_name
  template:
    src: "{{ some_template }}"
    dest: /etc/some/config/path/program_config
    owner: root
    group: root
    mode: 0644
  notify: restart_program # Can be used with handlers as well
...
```
