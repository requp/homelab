# Practical skills for day 4

### Register
It helps to make tasks below dependent on the current one if they use `when` with the register name

### Systemd module
Reload, restart, start, stop, enable, and disable services

### Docker compose
Start and stop Docker compose with state present and absent

### Creating users
```yaml
...
    - name: create user
      user:
        name: some_user
        group: root
        ...
...
```

### Send public keys
```yaml
...
    - name: add public key
      authorized_key:
        user: some_user
        key: 'some ssh key'
        ...
...
```
