# Django REST API - User Authentication & Review System

This is a Django REST Framework (DRF) project that provides APIs for user sign-up, login, and review management. Admin users have full control over all data, while regular users can manage their own reviews.

## Features

- User Registration (Sign Up)
- User Login with JWT Authentication
- Create, View, Delete Reviews
- Admin Dashboard to manage users and reviews
- Secure endpoints with permissions
- DRF-powered API views

---

## Technologies Used

- Python 3.x
- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt (for JWT auth)
- SQLite (default DB, can be switched to PostgreSQL, etc.)

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/your-drf-project.git
cd your-drf-project

## Create a virtual environment:

python -m venv venv

## Apply migrations:
- python manage.py makemigrations
- python manage.py migrate

## Install dependencies:
- pip install -r requirements.txt

## Run the server:
-- add a settings.py file
-- python manage.py runserver
