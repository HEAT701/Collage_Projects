# Architecture Documentation

## High-Level Design

The application uses a monolithic Django architecture split into domain-focused apps:

- Authentication and custom user management via `Employee` app.
- Business data domains separated by app: `Department`, `Role`, `Project`, `Leave`, `Attendance`.
- Aggregated owner-facing metrics provided by `Dashboard` app.

All domain entities are linked to `BusinessProfile` so owner data stays scoped to one business.

## App Boundaries

- **E_Managements**: root settings, URL routing, deployment entrypoints.
- **Employee**: custom auth model (`AUTH_USER_MODEL`) and owner/employee lifecycle.
- **Department/Role**: organizational structure and job catalog.
- **Project**: project tracking and assignment.
- **Leave/Attendance**: workforce operations and daily HR events.
- **Dashboard**: read-oriented aggregation layer.
- **Login_App**: login and logout endpoints.

## Data Ownership

`BusinessProfile` is the central ownership boundary.

Most domain models include a FK to `BusinessProfile`, and service functions/dashboard filters use `request.user.business_profile` to limit access.

## Validation Strategy

- Model-level `clean()` in Leave and Attendance prevents invalid date/time and business mismatch records.
- `Attendance` uses uniqueness constraint `(employee, date)`.

## Security Notes

Current implementation uses session-based auth and role checks in login redirection, but should be extended with role-based decorators and object-level access checks on all write endpoints.
