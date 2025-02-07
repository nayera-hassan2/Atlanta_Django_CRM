Django CRM Project

Overview

This is a Customer Relationship Management (CRM) system built with Django. It allows users to manage customer records efficiently, including adding, updating, and deleting customer details. The project uses Django's built-in authentication system for secure access.

Features

User authentication (Login/Logout)

View, add, update, and delete customer records

Search functionality for customer records

Modal-based customer record updates

Mobile-friendly and responsive design

Installation & Setup

Prerequisites

Ensure you have the following installed:

Python (>=3.8)

Django (>=4.0)

Virtualenv (optional but recommended)

Steps to Install

Clone the repository:

git clone https://github.com/nayera-hassan2/Atlanta_Django_CRM.git
cd Atlanta_Django_CRM

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Apply database migrations:

python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Follow the prompts to set up an admin user.

Run the development server:

python manage.py runserver

The project will be accessible at http://127.0.0.1:8000/.

Usage Instructions

Log in using the superuser credentials created earlier.

Navigate through the dashboard to manage customer records.

Use the modal forms to update customer details easily.

Delete or add new customer records as needed.

File Structure

Atlanta_Django_CRM/
│-- main/                  # Main Django app
│   │-- templates/main/    # HTML templates
│   │-- views.py           # Application views
│   │-- models.py          # Database models
│   │-- urls.py            # URL routing
│-- static/                # Static files (CSS, JS)
│-- manage.py              # Django management script
│-- requirements.txt       # Required Python packages
│-- db.sqlite3             # SQLite database (auto-generated)

Common Issues & Troubleshooting

1. NoReverseMatch: Reverse for 'index.html' not found

Solution: Ensure that index.html is correctly referenced as {% url 'main:index' %} in templates instead of {% url 'index.html' %}.


License

This project is open-source. Feel free to modify and enhance it as needed!

Author

Developed by Nayera Hassan.

