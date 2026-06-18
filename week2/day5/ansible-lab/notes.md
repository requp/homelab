# Practical skills for day 5
### Roles hierarchy

```
📁 some_dir/
│
├── 📄 playbook_with_role_names.yaml
│
└── 📁 roles/
    │
    ├── 📁 role1/
    │   ├── 📁 tasks/
    │   │   └── 📄 main.yaml
    │   ├── 📁 files/
    │   │   ├── 📄 some_file
    │   │   └── 📄 ...
    │
    ├── 📁 role2/
    │   ├── 📁 tasks/
    │   │   └── 📄 main.yaml
    │   ├── 📁 files/
    │   └── ...
    │
    └── 📁 ... (more roles)
```

#### Playbook with roles
```
...
- hosts: group1
  become: true
  roles: role1

- hosts: group2
  become: true
  roles: role2
...
```

#### Role main file
```
...
- name: copy file
  copy: 
    src: some_file
    dest: /path/to/target/
    ...
...
```
