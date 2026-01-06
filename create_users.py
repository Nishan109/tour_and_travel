#!/usr/bin/env python
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')
django.setup()

from django.contrib.auth.models import User

def create_test_users():
    print("Creating test users...")
    
    # Test users data
    users_data = [
        {'username': 'testuser1', 'email': 'test1@example.com', 'password': 'testpass123', 'first_name': 'John', 'last_name': 'Doe'},
        {'username': 'testuser2', 'email': 'test2@example.com', 'password': 'testpass123', 'first_name': 'Jane', 'last_name': 'Smith'},
        {'username': 'traveler1', 'email': 'traveler1@example.com', 'password': 'travel123', 'first_name': 'Mike', 'last_name': 'Johnson'},
        {'username': 'demo', 'email': 'demo@example.com', 'password': 'demo123', 'first_name': 'Demo', 'last_name': 'User'},
    ]
    
    for user_data in users_data:
        if not User.objects.filter(username=user_data['username']).exists():
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            print(f"Created user: {user.username} ({user.email})")
        else:
            print(f"User {user_data['username']} already exists")
    
    print("\nTest users created successfully!")
    print("\nYou can now login with any of these credentials:")
    print("Username: demo, Password: demo123")
    print("Username: testuser1, Password: testpass123")
    print("Username: traveler1, Password: travel123")
    print("\nOr use the superuser:")
    print("Username: root, Password: [the password you set]")

if __name__ == '__main__':
    create_test_users()