from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import LoginForm, ServiceForm
from .models import Service
from django.contrib.auth.models import User


def index(request):
#     username = 'john'
#     password = 'password123'

# # Create a new user instance
#     user = User.objects.create_user(username=username, password=password)

# # Save the user to the database
#     user.save()
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# @login_required
# def siparis(request):
#     return render(request, 'make_appointment.html')

def contact(request):
    return render(request, 'contact.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#     return render(request, 'login.html')

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/siparisal')
    else:
        form = LoginForm()
    return render(request, 'login.html')


    # def (request):
    # if request.method == 'POST':
    #     form = TicketForm(request.POST)
    #     if form.is_valid():
    #         # Save the form data to the database
    #         form.save()
    #         # Redirect to the form success page
    #         return redirect('form_success')
    # else:
    #     form = TicketForm()
    # return render(request, 'tickets/add_ticket.html', {'form': form})
@login_required
def service_form(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page
            return redirect('home')
    else:
        form = ServiceForm()

    return render(request, 'make_appointment.html', {'form': form})

def home(request):
    service = Service.objects.all()
    return render(request, 'home.html', {'service': service})
