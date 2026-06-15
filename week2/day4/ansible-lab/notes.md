# Practical skills for day 4

### Register
Helps to make tasks below dependent of the current if they use `when` with the register name

### Systemd module
Reload, restart, start, stop, enable and disable services

### Docker compose
start and stop docker compose with state present and absent

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
