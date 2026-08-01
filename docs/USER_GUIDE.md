# User Guide

## Owner Quick Start

1. Go to `/employee/owner_register/` and create owner account + business profile.
2. Login at `/Login_App/login_view/`.
3. Open `/Dashboard/dashboard_view/`.
4. Create master data first:
   - Department (`/Department/create_department/`)
   - Job role (`/Role/Job_create/`)
5. Create employees (`/employee/create_employee/`).
6. Record attendance (`/Attendance/Attendance/`).
7. Review/approve leave requests from dashboard actions.

## Employee Quick Start

1. Login via `/Login_App/login_view/`.
2. Open employee dashboard.
3. Submit leave requests through `/Leave/employee_leave_apply/`.

## Administrative Operations

- Open Django admin at `/admin/` with superuser credentials.
- Use admin for direct model inspection, corrections, and audits.

## Recommended Operational Practices

- Reset employee passwords immediately after creation.
- Enforce manager approvals and audit trail for leave.
- Back up SQLite DB regularly for local deployments.
