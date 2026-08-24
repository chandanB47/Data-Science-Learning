# Day 02: Data Definition Language (DDL)

## 1. What is DDL?
**Data Definition Language (DDL)** consists of SQL commands used to define, modify, and manage the structure of database objects (databases, tables, views, indexes).

* **Auto-commit**: In most RDBMS engines (like MySQL, Oracle), DDL operations are auto-committed and cannot be rolled back.
* **Metadata Focus**: DDL operations alter the database data dictionary/catalog rather than manipulating individual row contents.

---

## 2. Core DDL Commands

### A. `CREATE`
Used to initialize new database objects.

```sql
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    duration_weeks INT DEFAULT 4
);
