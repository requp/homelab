# Practical skills for day 2
## 1. pg_dump
### Typical command to dump a db
`pg_dump -U <db-user> -h <hostname> -p <port> -Fc -d <db> -f posible/path/<dump-name>`
- -Fc - for custom dump (can be also -Ft for tar archive and -Fd for dir)
- instead of `-d <db>` could be table with `-t <table>`

## 2. pg_restore
### Typical command to restore a db
`pg_restore -U <db-user> -h <hostname> -p <port> -F c <possible/path/<dump-name> -d <db>`
- a db with the given name has to exist already

## 3. DATABASE
### Show
#### Show all dbs or a specific db
`\l` or `\l <db-name>`

### Move
#### Move to another db
`\c <db-name>`

### Create
#### Create a db
```sql
CREATE DATABASE some-db;
```

#### Create a db declaring owner
```sql
CREATE DATABASE some-db
WITH OWNER user;
```

### Drop
#### Drop a db with no active connections
```sql
DROP DATABASE some-db;
```

#### Force drop any db
```sql
DROP DATABASE some-db WITH (FORCE);
```

## Role
Roles are like users in other DB systems. They have the same rights

### Common use
#### Show all roles
```sql
\du
```

#### Login as a role
```sql
psql -U manager
```

### Create
#### Create a role with a password 
```sql
CREATE ROLE manager
WITH LOGIN PASSWORD 'strongpass';
```

#### Create a superuser role
```sql
CREATE ROLE root
WITH LOGIN PASSWORD 'strongpass'
SUPERUSER;
```

### Alter
Everything here could be also added while creating roles. Or added later using `ALTER` statement.

#### Add an expiration date to a role 
```sql
ALTER ROLE manager
WITH VALID UNTIL '2026-08-01';
```

#### Limit connections by a role 
```sql
ALTER ROLE worker
WITH CONNECTION LIMIT 10;
```

### Drop a role

```sql
DROP ROLE manager;
```