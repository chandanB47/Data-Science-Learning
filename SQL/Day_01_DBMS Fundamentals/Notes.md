# Day 01: DBMS vs RDBMS & SQL Fundamentals

## 1. What is a Database?
A **Database** is an organized collection of structured data stored electronically in a computer system.

- **Data**: Raw facts and figures (e.g., numbers, text, timestamps).
- **Information**: Processed data that carries business context.
- **Database Management System (DBMS)**: Software that interacts with end users, applications, and the database itself to capture and analyze data.

---

## 2. DBMS vs. RDBMS

| Feature | DBMS (File/Hierarchical/Flat) | RDBMS (Relational Database) |
| :--- | :--- | :--- |
| **Data Storage** | Files, flat files, XML, hierarchical trees | Tabular format (Rows and Columns) |
| **Relationships** | No explicit relational mapping between entities | Enforces relationships via **Primary & Foreign Keys** |
| **Data Redundancy** | Common; lacks strict normalization rules | Minimized using **Normalization (1NF, 2NF, 3NF, BCNF)** |
| **Integrity & Constraints** | User-managed or application-level checks | Enforced directly by the database engine |
| **ACID Compliance** | Rarely supports strict ACID transactions | Fully supports **ACID** properties |
| **Data Volume & Scale** | Small to medium scale | Enterprise-scale, highly concurrent systems |
| **Examples** | XML files, MS Access, File System | PostgreSQL, MySQL, SQL Server, Oracle |

---

## 3. ACID Properties

Relational databases guarantee reliability through the **ACID** model:

* **Atomicity ("All or Nothing")**: A transaction cannot partially execute. If any part of a multi-step query fails, all changes are rolled back to the initial state.
* **Consistency**: Transactions bring the database from one valid state to another, strictly obeying all schema constraints, unique keys, and triggers.
* **Isolation**: Concurrent transactions execute independently without interfering with each other's uncommitted data.
* **Durability**: Once a transaction commits, the changes persist permanently in non-volatile storage, even during power outages or system crashes.

---

## 4. Relational Database Concepts

* **Table (Relation)**: A 2-dimensional grid of rows and columns.
* **Record (Row / Tuple)**: A single entity instance (e.g., one customer record).
* **Attribute (Column / Field)**: A characteristic describing the entity (e.g., `email`, `salary`).
* **Primary Key (PK)**: A column or set of columns uniquely identifying every row in a table. Must be unique and non-null.
* **Foreign Key (FK)**: A column in one table referencing the Primary Key of another table, establishing relational integrity.

---

## 5. Overview of SQL Sub-Languages

* **DDL (Data Definition Language)**: Defines structure (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`).
* **DML (Data Manipulation Language)**: Modifies records (`INSERT`, `UPDATE`, `DELETE`).
* **DQL (Data Query Language)**: Retrieves records (`SELECT`).
* **TCL (Transaction Control Language)**: Manages atomic units of work (`COMMIT`, `ROLLBACK`, `SAVEPOINT`).
* **DCL (Data Control Language)**: Manages permissions and security (`GRANT`, `REVOKE`).
