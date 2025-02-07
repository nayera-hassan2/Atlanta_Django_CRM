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

1. Ensure you have Python 3.8+ installed.

2. Clone the repository:

git clone https://github.com/nayera-hassan2/Atlanta_Django_CRM.git

3. Navigate to the project directory:

cd Atlanta_Django_CRM

4. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

5. Install the required dependencies:

pip install -r requirements.txt

6. Apply database migrations:

python manage.py migrate

7. Create a superuser:

python manage.py createsuperuser

8. Run the application:

python manage.py runserver

Usage

1. Log in to the admin panel using the superuser credentials.

2. Add, update, and manage customer records through the dashboard.

3. Use the search functionality to find specific customer details.

Technologies Used

> Python

> Django

> MySQL

> HTML, CSS, Javascript, Bootstrap

License

This project is open-source. Feel free to modify and enhance it as needed!

Author

Developed by Nayera Hassan.

