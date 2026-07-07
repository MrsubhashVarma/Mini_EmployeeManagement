# Employee Management System (Django REST API)

This is a REST API-based Employee Management System built using Django, Django REST Framework, and SQLite. It provides basic CRUD (Create, Read, Update, Delete) operations to manage employee records.

## Project Structure

```text
EmployeeManagement/
│── manage.py
├── EmployeeManagement/
│     settings.py
│     urls.py
└── employee/
      models.py
      serializers.py
      views.py
      urls.py
      migrations/
```

## Features & Endpoints

| Method | Endpoint | Description |
|:---|:---|:---|
| **POST** | `/employees/add/` | Add a new employee |
| **GET** | `/employees/` | Retrieve all employees |
| **PUT** | `/employees/update/<id>/` | Update employee details |
| **DELETE** | `/employees/delete/<id>/` | Delete an employee |

---

## Getting Started

### 1. Run Migrations
Run the migrations to set up the SQLite database schema:
```bash
cd EmployeeManagement
python manage.py migrate
```

### 2. Seed Test Data
Populate the database with the 5 required default employees:
```bash
python seed_employees.py
```

### 3. Run the Development Server
Start the local server:
```bash
python manage.py runserver
```

---

## Authentication & Administration

### Django Admin Panel
Access the administration panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) with:
*   **Username**: `admin`
*   **Password**: `admin`

### Browsable API Login
Authentication links for the DRF browsable interface:
*   **Login**: [http://127.0.0.1:8000/api-auth/login/](http://127.0.0.1:8000/api-auth/login/)
*   **Logout**: [http://127.0.0.1:8000/api-auth/logout/](http://127.0.0.1:8000/api-auth/logout/)

---

## Running Automated Tests
Run the test suite verifying all CRUD operations and JSON shapes:
```bash
python manage.py test
```

---

## API Payloads & Responses

### 1. Add Employee (`POST /employees/add/`)
**Request Body:**
```json
{
    "name": "Rahul Sharma",
    "email": "rahul@gmail.com",
    "phone": "9876543210",
    "department": "Software Development",
    "designation": "Python Developer",
    "salary": 65000,
    "city": "Hyderabad"
}
```
**Response (201 Created):**
```json
{
    "message": "Employee Added Successfully",
    "employee": {
        "id": 1,
        "name": "Rahul Sharma",
        "email": "rahul@gmail.com",
        "phone": "9876543210",
        "department": "Software Development",
        "designation": "Python Developer",
        "salary": 65000.0,
        "city": "Hyderabad"
    }
}
```

### 2. View All Employees (`GET /employees/`)
**Response (200 OK):**
```json
[
    {
        "id": 1,
        "name": "Rahul Sharma",
        "email": "rahul@gmail.com",
        "phone": "9876543210",
        "department": "Software Development",
        "designation": "Python Developer",
        "salary": 65000.0,
        "city": "Hyderabad"
    }
]
```

### 3. Update Employee (`PUT /employees/update/<id>/`)
**Request Body:**
```json
{
    "name": "Priya Reddy",
    "email": "priya.reddy@gmail.com",
    "phone": "9123456789",
    "department": "Human Resources",
    "designation": "Senior HR Executive",
    "salary": 55000,
    "city": "Hyderabad"
}
```
**Response (200 OK):**
```json
{
    "message": "Employee Updated Successfully",
    "employee": {
        "id": 2,
        "name": "Priya Reddy",
        "email": "priya.reddy@gmail.com",
        "phone": "9123456789",
        "department": "Human Resources",
        "designation": "Senior HR Executive",
        "salary": 55000.0,
        "city": "Hyderabad"
    }
}
```

### 4. Delete Employee (`DELETE /employees/delete/<id>/`)
**Response (200 OK):**
```json
{
    "message": "Employee Deleted Successfully"
}
```
