from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Employee

class EmployeeAPITests(APITestCase):
    def setUp(self):
        # We will define the sample test data here
        self.employee1_data = {
            "name": "Rahul Sharma",
            "email": "rahul@gmail.com",
            "phone": "9876543210",
            "department": "Software Development",
            "designation": "Python Developer",
            "salary": 65000.0,
            "city": "Hyderabad"
        }
        self.employee2_data = {
            "name": "Priya Reddy",
            "email": "priya@gmail.com",
            "phone": "9123456789",
            "department": "Human Resources",
            "designation": "HR Executive",
            "salary": 45000.0,
            "city": "Bangalore"
        }
        self.employee3_data = {
            "name": "Arjun Kumar",
            "email": "arjun@gmail.com",
            "phone": "9988776655",
            "department": "Testing",
            "designation": "QA Engineer",
            "salary": 55000.0,
            "city": "Chennai"
        }
        self.employee4_data = {
            "name": "Sneha Patel",
            "email": "sneha@gmail.com",
            "phone": "9012345678",
            "department": "UI/UX",
            "designation": "UI Designer",
            "salary": 50000.0,
            "city": "Pune"
        }
        self.employee5_data = {
            "name": "Vikram Singh",
            "email": "vikram@gmail.com",
            "phone": "9090909090",
            "department": "DevOps",
            "designation": "DevOps Engineer",
            "salary": 70000.0,
            "city": "Mumbai"
        }
        self.employee2_update_data = {
            "name": "Priya Reddy",
            "email": "priya.reddy@gmail.com",
            "phone": "9123456789",
            "department": "Human Resources",
            "designation": "Senior HR Executive",
            "salary": 55000.0,
            "city": "Hyderabad"
        }

    def test_crud_lifecycle(self):
        # 1. Create employees
        # Employee 1
        response = self.client.post('/employees/add/', self.employee1_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Employee Added Successfully")
        self.assertEqual(response.data['employee']['name'], "Rahul Sharma")
        self.assertEqual(response.data['employee']['id'], 1)

        # Employee 2
        response = self.client.post('/employees/add/', self.employee2_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Employee Added Successfully")
        self.assertEqual(response.data['employee']['id'], 2)

        # Employee 3
        response = self.client.post('/employees/add/', self.employee3_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Employee 4
        response = self.client.post('/employees/add/', self.employee4_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Employee 5
        response = self.client.post('/employees/add/', self.employee5_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 2. View all employees
        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        # Check matching of records
        self.assertEqual(response.data[0]['name'], "Rahul Sharma")
        self.assertEqual(response.data[1]['name'], "Priya Reddy")
        self.assertEqual(response.data[2]['name'], "Arjun Kumar")
        self.assertEqual(response.data[3]['name'], "Sneha Patel")
        self.assertEqual(response.data[4]['name'], "Vikram Singh")

        # 3. Update Employee ID = 2
        response = self.client.put('/employees/update/2/', self.employee2_update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Employee Updated Successfully")
        self.assertEqual(response.data['employee']['email'], "priya.reddy@gmail.com")
        self.assertEqual(response.data['employee']['designation'], "Senior HR Executive")
        self.assertEqual(response.data['employee']['salary'], 55000.0)
        self.assertEqual(response.data['employee']['city'], "Hyderabad")

        # Verify details of all employees database records after update
        # 1	Rahul Sharma	Software Development	Python Developer	65000	Hyderabad
        # 2	Priya Reddy	Human Resources	Senior HR Executive	55000	Hyderabad
        # (Wait, expected database records list states 2 Priya Reddy HR Executive 45000 Bangalore but that's pre-update or expected database list. Let's make sure the DB updates properly.)
        response_all = self.client.get('/employees/')
        self.assertEqual(response_all.data[1]['designation'], "Senior HR Executive")

        # 4. Delete Employee ID = 2
        response = self.client.delete('/employees/delete/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Employee Deleted Successfully")

        # Verify that employee ID 2 is deleted
        response_all = self.client.get('/employees/')
        self.assertEqual(len(response_all.data), 4)
        for emp in response_all.data:
            self.assertNotEqual(emp['id'], 2)
