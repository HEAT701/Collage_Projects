# Bug Report (Static Audit + Environment Test Run)

Date: 2026-02-14
Scope: Entire repository source audit (`*.py`, templates) and runnable checks available in current environment.

---

## Environment/Execution Findings

1. `python manage.py check` failed because Django is not installed in runtime environment.
2. Installing dependencies with `pip install -r requirements.txt` failed due proxy/network restriction (`403 Forbidden`).
3. Python syntax compilation across repo passed (`python -m compileall -q .`).

---

## Confirmed Bugs

## BUG-001: Invalid field name in employee query (`roal` instead of `role`)
- **Severity:** High
- **Impact:** Employee listing service raises `FieldError` when called.
- **Location:** `Employee/servies.py`
- **Code:** `Employee.objects.filter(roal='employee', is_active=True)`
- **Why bug:** Model field is `role`, not `roal`.
- **Fix suggestion:** Replace `roal` with `role`.

---

## BUG-002: Broken login redirect configuration in `login_required`
- **Severity:** Medium
- **Impact:** Unauthorized access redirect can fail due invalid URL name.
- **Location:** `Dashboard/views.py`
- **Code:** `@login_required(login_url='Login_App:login/')`
- **Why bug:** URL pattern is named `login_view`, not `login/`.
- **Fix suggestion:** `@login_required(login_url='Login_App:login_view')`.

---

## BUG-003: Template name case mismatch for login page
- **Severity:** High (Linux/case-sensitive FS)
- **Impact:** Login page rendering can throw `TemplateDoesNotExist`.
- **Location:** `Login_App/views.py` + `templates/login.html`
- **Code:** `return render(request, 'Login.html')`
- **Why bug:** Actual file present is `templates/login.html` (lowercase).
- **Fix suggestion:** Render `'login.html'` or rename template consistently.

---

## BUG-004: Leave apply view uses non-existent reverse relation (`request.user.employee`)
- **Severity:** High
- **Impact:** Raises `AttributeError` during employee leave submit.
- **Location:** `Leave/views.py`
- **Code:** `employee = request.user.employee`
- **Why bug:** `request.user` already is `Employee` (`AUTH_USER_MODEL`); no `.employee` relation needed.
- **Fix suggestion:** `employee = request.user`.

---

## BUG-005: `Project_view` can reference `form` before assignment
- **Severity:** High
- **Impact:** GET request to project page can raise `UnboundLocalError`.
- **Location:** `Project/views.py`
- **Code path:** `return render(..., {'form': form})` while `form` only set in POST branch.
- **Fix suggestion:** Add `else: form = ProjectForm()` before render.

---

## Risk/Quality Issues (Not immediate crash but problematic)

## RISK-001: Dead/duplicate service snippet with same typo
- **Location:** `Dashboard/servies.py`
- **Detail:** A commented old `Get_Employee_view` also uses typo `roal`, increases maintenance confusion.

## RISK-002: Inconsistent naming typos across service modules
- **Locations:** `Employee/servies.py`, `Dashboard/servies.py`
- **Detail:** `servies`, `fiend_Total_deparment`, `Get_Employee_view` naming inconsistencies reduce maintainability.

---

## Recommended Priority Order

1. Fix BUG-001, BUG-003, BUG-004, BUG-005 first (runtime blockers/crashes).
2. Fix BUG-002 next (auth flow correctness).
3. Clean RISK issues for maintainability and future regression prevention.

---

## Commands Used

- `python -m compileall -q .`
- `python manage.py check`
- `python -m pip install -r requirements.txt`
- `rg -n "..."` scans for suspect patterns
- `nl -ba <file>` for line-precise verification
