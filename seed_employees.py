import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmployeeManagement.settings')
django.setup()

from employee.models import Employee

# Clear existing data to allow re-runs
Employee.objects.all().delete()

# Test data
employees = [
    {
        "id": 1,
        "name": "Rahul Sharma",
        "email": "rahul@gmail.com",
        "phone": "9876543210",
        "department": "Software Development",
        "designation": "Python Developer",
        "salary": 65000,
        "city": "Hyderabad"
    },
    {
        "id": 2,
        "name": "Priya Reddy",
        "email": "priya@gmail.com",
        "phone": "9123456789",
        "department": "Human Resources",
        "designation": "HR Executive",
        "salary": 45000,
        "city": "Bangalore"
    },
    {
        "id": 3,
        "name": "Arjun Kumar",
        "email": "arjun@gmail.com",
        "phone": "9988776655",
        "department": "Testing",
        "designation": "QA Engineer",
        "salary": 55000,
        "city": "Chennai"
    },
    {
        "id": 4,
        "name": "Sneha Patel",
        "email": "sneha@gmail.com",
        "phone": "9012345678",
        "department": "UI/UX",
        "designation": "UI Designer",
        "salary": 50000,
        "city": "Pune"
    },
    {
        "id": 5,
        "name": "Vikram Singh",
        "email": "vikram@gmail.com",
        "phone": "9090909090",
        "department": "DevOps",
        "designation": "DevOps Engineer",
        "salary": 70000,
        "city": "Mumbai"
    }
]

for emp_data in employees:
    Employee.objects.create(**emp_data)

print("Database seeded successfully with 5 employees.")
