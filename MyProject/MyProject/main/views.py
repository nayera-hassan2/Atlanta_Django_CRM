from django.shortcuts import render, redirect
from .scripts.sign_in_form import setup_logger, perform_login
from django.contrib.auth import logout
from django.contrib import messages
from .models import Quote, ContactUs, CareerApplication, CustomersRecords, EmployeesRecords
from django.http import HttpResponse


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


def get_a_quote_records(request):
    # Fetching Quote records
    get_a_quote_records = Quote.objects.all()

    # Passing the records to the context
    context = {'get_a_quote_records': get_a_quote_records}

    return render(request, 'main/index.html', context)


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


def contact_us_records(request):
    # Fetching ContactUs records
    contact_us_records = ContactUs.objects.all()

    # Passing the records to the context
    context = {'contact_us_records': contact_us_records}

    return render(request, 'main/index.html', context)


def customer_records(request):
    # Fetching Customer records
    customer_records = CustomersRecords.objects.all()

    #   Passing the records to the context
    context = {'customer_records': customer_records}
    
    
    # Print records to the console
    # for record in customer_records:
    #     print(f"First Name: {record.first_name}")
    #     print(f"Last Name: {record.last_name}")
    #     print(f"Email: {record.email}")
    #     print(f"Phone Number: {record.phone_number}")
    #     print(f"Address: {record.address}")
    #     print(f"City: {record.city}")
    #     print(f"State: {record.state}")
    #     print(f"Zipcode: {record.zipcode}")
    #     print(f"Created At: {record.created_at}")
    #     print("-" * 30) 

    # Optionally, you can return a response to the browser
    # return HttpResponse("Customer records printed in the console.")
        
    # Rendering the data in the index.html template
    return render(request, 'main/index.html', context)


def employees_records(request):
    # Fetching Employee records
    employees_records = EmployeesRecords.objects.all()

    # Print the fetched records to the console
    for record in employees_records:
        print(f"Employee: {record.first_name} {record.last_name}")

    # Passing the records to the context
    context = {'employees_records': employees_records}

    return render(request, 'main/index.html', context)


def career(request):
    if request.method == 'POST':
        # Get form data from the POST request
        username = request.POST.get('username')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        text = request.POST.get('text')  # Assuming this should be a DateField
        address = request.POST.get('address')
        file = request.FILES.get('file') 
        message = request.POST.get('message')

        # Create a new CareerApplication object and save it to the database
        career_entry = CareerApplication(
            username=username,
            email=email,
            tel=tel,
            text=text,
            address=address,
            file=file,
            message=message
        )
        career_entry.save()

        messages.success(request, 'Career form submitted successfully!')

        # Redirect to the same page to avoid form resubmission on refresh
        return redirect('main:career')

    return render(request, 'main/career.html')


def career_records(request):
    # Fetching CareerApplication records
    career_records = CareerApplication.objects.all()

    # Print the absolute paths to debug
    for record in career_records:
        print(f"File Path: {record.file.path}")

    # Passing the records to the context
    context = {'career_records': career_records}

    return render(request, 'main/index.html', context)