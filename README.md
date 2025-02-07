Django CRM Project

Overview

This is a Customer Relationship Management (CRM) system built with Django. It allows users to manage customer records efficiently, including adding, updating, and deleting customer details. The project uses Django's built-in authentication system for secure access.

Features

User authentication (Login/Logout).

View, add, update, and delete customer records.

Search functionality for customer records.

Modal-based customer record updates.

Mobile-friendly and responsive design.

Integrated database for storing customer data.

Installation

Follow these steps to set up the project:

Ensure you have Python 3.8+ installed.

Clone the repository:

git clone https://github.com/nayera-hassan2/Atlanta_Django_CRM.git

Navigate to the project directory:

cd Atlanta_Django_CRM

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:

pip install -r requirements.txt

Apply database migrations:

python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Run the application:

python manage.py runserver

Usage

Log in to the admin panel using the superuser credentials.

Add, update, and manage customer records through the dashboard.

Use the search functionality to find specific customer details.

Technologies Used

Python

Django

MySQL

HTML, CSS, Javascript, Bootstrap

License

This project is open-source. Feel free to modify and enhance it as needed!

Author

Developed by Nayera Hassan.

