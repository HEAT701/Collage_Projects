# HTML Data Display Code Extract

Ye document un HTML templates ka **main code extract** deta hai jahan dynamic data (`{{ ... }}` / `{% for ... %}`) show kiya ja raha hai.

---

## 1) `templates/dashboard.html`

### A) Dashboard cards (counts)
```html
<p class="text-3xl font-black mt-1">{{total_employees}}</p>
<p class="text-3xl font-black mt-1">{{Total_departments.count}}</p>
<p class="text-3xl font-black mt-1">{{today_attendance.count}}</p>
<p class="text-3xl font-black mt-1">{{pending_leaves}}</p>
```

### B) Recent employees table
```html
{% for emp in recentadd_employees %}
<tr class="border-b border-slate-100 last:border-none hover:bg-slate-50 transition group">
    <td class="py-4">
        <div class="flex items-center gap-3">
            <div class="w-9 h-9 bg-indigo-100 rounded-lg flex items-center justify-center font-bold text-indigo-600">
                {{ emp.first_name|slice:":1" }}
            </div>
            <div>
                <p>{{ emp.first_name }} {{ emp.last_name }}</p>
                <p class="text-[10px] text-slate-400 font-medium">{{ emp.job.title }}</p>
            </div>
        </div>
    </td>
    <td class="py-4 text-slate-500 font-medium">{{ emp.phone }}</td>
    <td class="py-4 text-slate-500 font-medium">{{ emp.hire_date|date:"d M, Y" }}</td>
</tr>
{% endfor %}
```

### C) Attendance table
```html
{% for att in today_attendance %}
<tr class="border-b border-slate-100">
    <td class="py-4 font-bold">{{ att.employee }}</td>
    <td class="py-4 text-slate-500">{{ att.check_in }}</td>
    <td class="py-4 text-slate-500">{{ att.check_out }}</td>
    <td class="py-4 font-bold">{{ att.Total_hours }}</td>
</tr>
{% endfor %}
```

### D) Pending leave cards
```html
{% for leave in pending_leave_list %}
<div class="bg-white border border-slate-100 rounded-2xl p-4 shadow-sm">
    <p class="font-bold text-slate-800">{{ leave.employee }}</p>
    <p class="text-xs text-slate-400">{{ leave.start_date }} - {{ leave.end_date }}</p>
</div>
{% endfor %}
```

### E) Departments display
```html
{% for dept in Total_departments %}
<div class="bg-white p-6 rounded-3xl border border-slate-100 shadow-sm hover:shadow-md transition">
    <h4 class="text-xl font-black text-slate-800">{{ dept.name }}</h4>
    <p class="text-sm text-slate-400 mb-6">{{ dept.total_employees }} Team Members</p>
</div>
{% endfor %}
```

---

## 2) `templates/Employee_Detail.html`

### Employee profile data
```html
<h1 class="text-3xl font-black text-slate-800 tracking-tight">
    {{ employee.first_name }} {{ employee.last_name }}
</h1>
<p class="text-slate-400 font-semibold mt-2">{{ employee.job.title|default:"Executive" }}</p>
<span class="px-3 py-1 bg-slate-50 text-slate-500 rounded-full text-[10px] font-bold">{{ employee.department.name|default:"General" }}</span>

<p class="text-sm font-semibold text-slate-700">{{ employee.email|default:"user@emspro.com" }}</p>
<p class="text-sm font-semibold text-slate-700">{{ employee.phone }}</p>
<p class="text-2xl font-black text-slate-800 mt-1">₹{{ employee.salary }}</p>

<p class="text-lg font-bold text-slate-700">#EMS-00{{ employee.id }}</p>
<p class="text-lg font-bold text-slate-700">{{ employee.hire_date|date:"d F, Y" }}</p>
```

---

## 3) `templates/Department_Detail.html`

### Department details data
```html
{{ department.name }}
<span class="text-xl font-bold text-slate-700">#{{ department.id }}</span>
<span class="text-xl font-bold text-slate-700">{{ department.total_employees }} Employees</span>
"{{ department.description|default:'No description available for this department.' }}"
```

---

## 4) `templates/Department.html`

### Department list/table display
```html
{% for dept in departments %}
<tr class="border-b border-slate-100 last:border-none hover:bg-slate-50 transition-all group">
    <td class="px-8 py-5 text-sm font-black text-slate-400">{{ forloop.counter }}</td>
    <td class="px-8 py-5">
        <p class="font-bold text-slate-800 text-lg group-hover:text-indigo-600 transition-colors">{{ dept.name }}</p>
    </td>
</tr>
{% endfor %}
```

---

## 5) `templates/Employee_Dashboard.html`

### Logged-in employee and business data
```html
<span class="text-sm font-extrabold text-slate-800">{{ request.user.business_profile.business_name}}</span>
<span class="text-sm font-extrabold text-slate-800">{{request.user.first_name}} {{request.user.last_name}}</span>
<span class="text-[10px] font-bold text-indigo-500 uppercase">{{request.user.role}}</span>

<h1 class="text-3xl font-black text-slate-800">{{request.user.first_name}} {{request.user.last_name}}</h1>
<p class="font-bold text-sm text-slate-700">{{request.user.email}}</p>
<p class="font-bold text-sm text-slate-700">{{request.user.date_joined}}</p>
```

### Leave type dynamic options
```html
{% for lt in leave_types %}
<option value="{{ lt }}">{{ lt }}</option>
{% endfor %}
```

---

## 6) `templates/Create_Employee.html`

### Dynamic dropdown data (department/job)
```html
{% for dept in departments %}
<option value="{{ dept.id }}">{{ dept.name }}</option>
{% endfor %}

{% for job in jobs %}
<option value="{{ job.id }}">{{ job.title }}</option>
{% endfor %}
```

---

## 7) Other templates with dynamic form rendering

In files below, dynamic Django form object render kiya gaya hai (form fields as data-bound UI):

- `templates/Attendance.html` → `{{form}}`
- `templates/Employee_Update.html` → `{{ form.first_name }}`, `{{ form.last_name }}`, `{{ form.email }}`, `{{ form.phone }}`, `{{ form.hire_date }}`, `{{ form.salary }}`, `{{ form.department }}`, `{{ form.job }}`
- `templates/Job.html` → `{{ form.title }}`, `{{ form.department }}`, `{{ form.job_type }}`, `{{ form.salary_range }}`, `{{ form.location }}`, `{{ form.description }}`

---

## Quick Conclusion

Jitne major HTML pages me **data show** ho raha hai, unka main display code upar extract kar diya gaya hai:
- dashboard analytics + lists
- employee detail profile
- department detail and list
- employee dashboard profile + leave types
- create employee dropdown bindings
