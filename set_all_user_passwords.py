import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmployeeManagement.settings')
django.setup()

from django.contrib.auth.models import User

PASSWORD = 'Scarface$007'


def main():
    users = User.objects.all()
    print(f'Updating password for {users.count()} user(s)...')

    for user in users:
        user.set_password(PASSWORD)
        user.save()

    print('Done. All user passwords have been updated to Scarface$007.')


if __name__ == '__main__':
    main()
