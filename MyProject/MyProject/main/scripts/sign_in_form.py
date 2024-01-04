import re
from django.contrib import messages
import logging
from main import views
from ..models import LoginData
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


def setup_logger():
    logging.basicConfig(filename='Login_log_file.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def validate_email(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(re.match(email_pattern, email))


def validate_password(password):
   return len(password) >= 8  # Minimum password length of 8 characters


def validate_login(email, password):
    return validate_email(email) and validate_password(password)


def perform_login(request, email, password):
    if validate_login(email, password):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print("User not found.")
            logging.error(f'Failed login attempt for email: {email} - User not found.')
            messages.error(request, "Login failed. User not found.")
            return False

        if check_password(password, user.password):
            if user.is_active:
                login(request, user)
                logging.info(f'Successful login attempt for email: {email}')
                messages.success(request, "Login successful!")
                return True
            else:
                print("User is not active.")
                logging.error(f'Failed login attempt for email: {email} - User is not active.')
                messages.error(request, "Account is not active. Please contact support.")
        else:
            print("Password does not match.")
            logging.error(f'Failed login attempt for email: {email} - Password does not match.')
            messages.error(request, "Login failed. Please check your credentials.")
    else:
        print("Invalid email or password.")
        logging.error(f'Invalid email or password for login attempt for email: {email}')
        messages.error(request, "Invalid email or password. Please check your credentials.")

    return False


if __name__ == "__main__":
    setup_logger()
    perform_login()