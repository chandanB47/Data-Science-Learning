# Day 25: DCL & Database Security

## 🎯 Key Learning Objectives
* Understand how MySQL identifies and authenticates accounts (`'username'@'hostname'`).
* Master the Data Control Language commands: `GRANT` and `REVOKE`.
* Understand the privilege hierarchy: Global, Database, Table, and Column levels.
* Simplify access management for analytics teams using Roles.
* Learn why `FLUSH PRIVILEGES` is used and when it is actually necessary.


--- 
### 1. What is DCL (Data Control Language)?
Data Control Language (DCL) consists of SQL statements that control access privileges, permissions, and security parameters within the database management system.

The two foundational commands are:

* GRANT: Authorizes a user or role to perform specified operations on designated database objects.

* REVOKE: Removes previously authorized privileges from a user or role.

### 2. MySQL User Identification (user@host)
In MySQL, an account is defined by both a username and the network host from which the user connects:

* 'analyst'@'localhost': User can connect only from the local machine running MySQL.

* 'analyst'@'192.168.1.%': User can connect from any machine on the 192.168.1.x subnet.

* 'analyst'@'%': User can connect from any IP address (wildcard).

```SQL
-- Create an account
CREATE USER 'chandan_analyst'@'localhost' IDENTIFIED BY 'StrongP@ssw0rd2026!';
```

### 3. Role-Based Access Control (RBAC)
Managing permissions on individual user accounts becomes difficult as teams grow. 
Instead, define Roles (collections of privileges) and assign those roles to users:

```Plaintext


       [ Role: read_only_analyst ]
        ├── GRANT SELECT ON retail_analytics.*
        └── GRANT SHOW VIEW ON retail_analytics.*
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
[ User: analyst_aarav ]   [ User: analyst_priya ]


```
#### Steps to Use Roles:

1. CREATE ROLE 'role_name';
2. Grant permissions to the role: GRANT SELECT ON db.* TO 'role_name';
3. Assign role to users: GRANT 'role_name' TO 'user_name'@'localhost';
4. Set default active role: SET DEFAULT ROLE ALL TO 'user_name'@'localhost';


### 4. Inspecting & Revoking Permissions

```SQL
-- View all privileges granted to a user
SHOW GRANTS FOR 'chandan_analyst'@'localhost';

-- Revoke write access while preserving read access
REVOKE INSERT, UPDATE, DELETE ON retail_analytics.* FROM 'chandan_analyst'@'localhost';

-- Delete the user account
DROP USER IF EXISTS 'chandan_analyst'@'localhost';

```

#### 💡 When is FLUSH PRIVILEGES necessary?

```Plaintext

FLUSH PRIVILEGES is only required when directly modifying the underlying MySQL grant tables using DML (e.g., UPDATE mysql.user ...).
When using standard account management statements (CREATE USER, GRANT, REVOKE, ALTER USER),
 the server updates in-memory privilege caches automatically.

```
