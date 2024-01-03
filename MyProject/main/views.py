from django.shortcuts import render, redirect
from .scripts.sign_in_form import setup_logger, perform_login
from django.contrib.auth import logout
from django.contrib import messages
from .models import Quote
from .models import ContactUs


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        setup_logger()

        if perform_login(request, email, password):
            # Redirecting to index on successful login
            return redirect('main:index')

    return render(request, 'main/sign-in.html')
    
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have Logged out Succesfully!" )    
    return redirect('main:sign-in')


def get_a_quote(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('tel')
        security_type = request.POST.get('security-type')
        message = request.POST.get('message')

        # Creating a new Quote object and saving it to the crm database
        quote = Quote(name=name, email=email, phone_number=phone_number, security_type=security_type, message=message)
        quote.save()

        messages.success(request, 'Quote submitted successfully!')

    return render(request, 'main/get-a-quote.html')


def contact_us(request):
    if request.method == 'POST':
        # Get form data from the POST request
        username = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new ContactUs object and save it to the database
        contact_entry = ContactUs(username=username, email=email, message=message)
        contact_entry.save()

        messages.success(request, 'Contact form submitted successfully!')

        # Redirect to the same page to avoid form resubmission on refresh
        return redirect('main:contact_us')

    return render(request, 'main/contact-us.html')