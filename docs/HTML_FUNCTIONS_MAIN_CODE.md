# HTML Function Audit – Main Code Extract

Is document me templates ke andar jo functional JavaScript logic add hai, uska **main code extract** diya gaya hai.

---

## Scope Checked

- `templates/dashboard.html`
- `templates/Department.html`
- `templates/Employee_Dashboard.html`
- `templates/Create_Employee.html`
- Inline handlers in other templates (`onclick="history.back()"`, confirm dialogs, etc.)

---

## 1) `dashboard.html` – Sidebar tab switching

**Location:** `templates/dashboard.html:329-354`

```html
<script>
    function showTab(element, tabId) {
        // 1. Sidebar Links Reset
        document.querySelectorAll('.sidebar-link').forEach(link => {
            link.classList.remove('active');
            link.classList.add('text-slate-400');
        });

        // 2. Active Sidebar Styling
        element.classList.add('active');
        element.classList.remove('text-slate-400');

        // 3. Tab Switching Logic
        document.querySelectorAll('.tab-content').forEach(tab => {
            tab.classList.remove('active');
        });
        const targetTab = document.getElementById(tabId);
        if (targetTab) {
            targetTab.classList.add('active');
        }

        // 4. Update Header Title
        const tabName = element.innerText.trim();
        document.getElementById('tab-title').innerText = tabName;
    }
</script>
```

---

## 2) `Department.html` – Department form toggle

**Location:** `templates/Department.html:139-149`

```html
<script>
    function toggleForm() {
        const form = document.getElementById('addDeptForm');
        if (form.classList.contains('hidden')) {
            form.classList.remove('hidden');
            form.scrollIntoView({ behavior: 'smooth' });
        } else {
            form.classList.add('hidden');
        }
    }
</script>
```

---

## 3) `Employee_Dashboard.html` – Employee tab switching

**Location:** `templates/Employee_Dashboard.html:196-203`

```html
<script>
    function switchTab(tabId, element) {
        document.querySelectorAll('button').forEach(btn => btn.classList.remove('active-link'));
        element.classList.add('active-link');
        document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
        document.getElementById(tabId).classList.add('active');
    }
</script>
```

---

## 4) `Create_Employee.html` – Form progress state logic

**Location:** `templates/Create_Employee.html:206-216`

```html
<script>
    const form = document.getElementById('employeeForm');
    const progressBar = document.getElementById('progressBar');

    form.addEventListener('focusin', (e) => {
        const name = e.target.name;
        if (['first_name', 'last_name', 'email'].includes(name)) progressBar.style.width = '35%';
        else if (['department', 'job', 'hire_date'].includes(name)) progressBar.style.width = '70%';
        else if (['salary', 'phone'].includes(name)) progressBar.style.width = '90%';
    });
</script>
```

---

## 5) Other inline functional handlers (quick list)

### Navigation / tab actions
- `templates/dashboard.html`: multiple `onclick="showTab(this, '...')"` bindings for sidebar tabs.
- `templates/Employee_Dashboard.html`: buttons use `onclick="switchTab('...', this)"`.
- `templates/Department.html`: button uses `onclick="toggleForm()"`.

### Browser back handlers
- `templates/Job.html`: `onclick="history.back()"`
- `templates/Employee_Update.html`: `onclick="history.back()"`
- `templates/Create_Employee.html`: `onclick="window.history.back()"`

### Confirm handlers
- `templates/dashboard.html`: delete action with `onclick="return confirm('Are you sure?')"`
- `templates/Department_Detail.html`: delete link with confirmation.

---

## Final Note

Aapke HTML me core custom functions mainly ye 3 declared functions hain:
1. `showTab(...)`
2. `toggleForm(...)`
3. `switchTab(...)`

Aur `Create_Employee.html` me ek functional event-listener based logic hai (`focusin` progress update), jisko upar main code ke roop me include kiya gaya hai.
