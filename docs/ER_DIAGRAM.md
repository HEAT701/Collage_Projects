# Entity Relationship Diagram (Models Database)

This ER diagram represents the current Django models and relationships across apps:
- `Employee` (custom auth model)
- `BusinessProfile`
- `Department`
- `Job`
- `Project`
- `Leave`
- `Attendance`
- Project–Employee many-to-many join

---

## ER Diagram (Mermaid)

```mermaid
erDiagram
    BUSINESS_PROFILE ||--o{ EMPLOYEE : owns
    BUSINESS_PROFILE ||--o{ DEPARTMENT : has
    BUSINESS_PROFILE ||--o{ JOB : has
    BUSINESS_PROFILE ||--o{ PROJECT : has
    BUSINESS_PROFILE ||--o{ LEAVE : scopes
    BUSINESS_PROFILE ||--o{ ATTENDANCE : scopes

    DEPARTMENT ||--o{ EMPLOYEE : contains
    JOB ||--o{ EMPLOYEE : assigned_to
    EMPLOYEE ||--o{ EMPLOYEE : manages

    EMPLOYEE ||--o{ LEAVE : requests
    EMPLOYEE ||--o{ LEAVE : approves
    EMPLOYEE ||--o{ ATTENDANCE : marks

    PROJECT ||--o{ PROJECT_EMPLOYEES : includes
    EMPLOYEE ||--o{ PROJECT_EMPLOYEES : assigned

    BUSINESS_PROFILE {
      bigint id PK
      string business_name
      string business_address
      string business_phone
      string business_email
    }

    EMPLOYEE {
      bigint id PK
      string username UK
      string email
      string role
      bigint business_profile_id FK
      string phone
      date hire_date
      decimal salary
      bigint department_id FK
      bigint job_id FK
      bigint manager_id FK
      bool is_active
      datetime date_joined
    }

    DEPARTMENT {
      bigint id PK
      string name
      text description
      bigint business_profile_id FK
    }

    JOB {
      bigint id PK
      string title
      text description
      bigint business_profile_id FK
    }

    PROJECT {
      bigint id PK
      string name
      text description
      bigint business_profile_id FK
      date start_date
      date end_date
    }

    PROJECT_EMPLOYEES {
      bigint id PK
      bigint project_id FK
      bigint employee_id FK
    }

    LEAVE {
      bigint id PK
      bigint employee_id FK
      bigint business_profile_id FK
      string leave_type
      date start_date
      date end_date
      text reason
      string status
      bigint approved_by_id FK
      datetime applied_on
    }

    ATTENDANCE {
      bigint id PK
      bigint employee_id FK
      bigint business_profile_id FK
      date date
      time check_in
      time check_out
      string status
    }
```

---

## Notes

- `Employee` is the active `AUTH_USER_MODEL`.
- `Attendance` has unique constraint on (`employee`, `date`).
- `Project_EMPLOYEES` is the auto-generated join table for `Project.employees` many-to-many field.
- `Leave.approved_by` and `Employee.manager` are self/employee references.
