```sql
-- ==========================================================
-- Day 14: Outer Joins (LEFT, RIGHT, FULL OUTER) Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Data
DROP TABLE IF EXISTS project_assignments;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS team_members;

CREATE TABLE team_members (
    member_id INT PRIMARY KEY,
    member_name VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL
);

CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    budget DECIMAL(12, 2) NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE project_assignments (
    assignment_id INT PRIMARY KEY,
    member_id INT,
    project_id INT,
    allocated_hours INT NOT NULL,
    CONSTRAINT fk_pa_member FOREIGN KEY (member_id) REFERENCES team_members(member_id),
    CONSTRAINT fk_pa_project FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

INSERT INTO team_members (member_id, member_name, role, department)
VALUES 
    (1, 'Aarav Sharma', 'Lead Data Scientist', 'Analytics'),
    (2, 'Neha Patel', 'Data Engineer', 'Engineering'),
    (3, 'Rohan Verma', 'Backend Engineer', 'Engineering'),
    (4, 'Priya Nair', 'BI Analyst', 'Analytics'),
    (5, 'Vikram Singh', 'DevOps Engineer', 'Infrastructure'); -- Not assigned to any project

INSERT INTO projects (project_id, project_name, budget, status)
VALUES 
    (101, 'Customer Churn Model', 250000.00, 'IN_PROGRESS'),
    (102, 'Realtime Analytics Pipeline', 400000.00, 'IN_PROGRESS'),
    (103, 'Cloud Migration', 150000.00, 'PLANNING'),
    (104, 'Legacy Deprecation', 50000.00, 'PROPOSED'); -- Has zero team members allocated

INSERT INTO project_assignments (assignment_id, member_id, project_id, allocated_hours)
VALUES 
    (1, 1, 101, 120),
    (2, 4, 101, 80),
    (3, 2, 102, 160),
    (4, 3, 102, 140),
    (5, 2, 103, 40);

-- ==========================================================
-- 2. LEFT JOIN: All Team Members & Assigned Projects
-- ==========================================================

-- Preserves all members (Vikram Singh shows NULLs for project details)
SELECT 
    m.member_id,
    m.member_name,
    m.role,
    p.project_name,
    pa.allocated_hours
FROM team_members m
LEFT JOIN project_assignments pa ON m.member_id = pa.member_id
LEFT JOIN projects p ON pa.project_id = p.project_id
ORDER BY m.member_id;

-- ==========================================================
-- 3. The Anti-Join Pattern: Finding Unassigned Resources
-- ==========================================================

-- Identify bench resources (team members with NO active project assignments)
SELECT 
    m.member_id,
    m.member_name,
    m.role,
    m.department
FROM team_members m
LEFT JOIN project_assignments pa ON m.member_id = pa.member_id
WHERE pa.assignment_id IS NULL;

-- Identify unstaffed projects (projects with NO team members allocated)
SELECT 
    p.project_id,
    p.project_name,
    p.budget,
    p.status
FROM projects p
LEFT JOIN project_assignments pa ON p.project_id = pa.project_id
WHERE pa.assignment_id IS NULL;

-- ==========================================================
-- 4. FULL OUTER JOIN: Complete Reconciliation
-- ==========================================================

-- Full picture: Shows assigned, unassigned members, AND unstaffed projects
SELECT 
    COALESCE(m.member_name, 'Unassigned / Open Role') AS team_member,
    COALESCE(p.project_name, 'No Active Project') AS project_name,
    pa.allocated_hours
FROM team_members m
FULL OUTER JOIN project_assignments pa ON m.member_id = pa.member_id
FULL OUTER JOIN projects p ON pa.project_id = p.project_id
ORDER BY team_member, project_name;

-- ==========================================================
-- 5. Trap Demonstration: Filtering in ON vs WHERE
-- ==========================================================

-- Filter in ON: Preserves ALL members, but only matches hours for project 101
SELECT 
    m.member_name,
    pa.allocated_hours
FROM team_members m
LEFT JOIN project_assignments pa 
    ON m.member_id = pa.member_id 
   AND pa.project_id = 101;

-- Filter in WHERE: Silently eliminates members not on project 101 (Acting like INNER JOIN)
SELECT 
    m.member_name,
    pa.allocated_hours
FROM team_members m
LEFT JOIN project_assignments pa ON m.member_id = pa.member_id
WHERE pa.project_id = 101;
