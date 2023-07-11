from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Car, Account
from .forms import CarSellForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
import time

def home(request):
    return render(request, 'index.html', context={'user': request.user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the catalog page upon successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

def services(request):
    template = loader.get_template('service.html')
    return HttpResponse(template.render())

@login_required
def catalog(request):
    cars = Car.objects.all()
    return render(request, 'catalog.html', {'cars': cars})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def sell_car(request):
    if request.method == 'POST':
        form = CarSellForm(request.POST, request.FILES)
        if form.is_valid():
            # Retrieve the form data
            make = form.cleaned_data['make']
            model = form.cleaned_data['model']
            year = form.cleaned_data['year']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']

            # Save the data in the Car model
            car = Car(make=make, model=model, year=year, price=price, image=image)
            car.save()

            return redirect('catalog')  # Replace 'catalog' with the appropriate URL name for your catalog page
    else:
        form = CarSellForm()

    return render(request, 'sell_car.html', {'form': form})

def checkout(request):
    if request.method == 'POST':
        # Process the form data
        # You can access the submitted form data using `request.POST` dictionary
        # For example:
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        payment = request.POST['payment']

        # Perform any necessary processing with the form data

        # Redirect to the success page
        return redirect('success')

    # Handle GET request or invalid POST request
    return redirect('home')  # Replace 'home' with the appropriate URL name for your home page

def success(request):
    # Render the success page with the message
    return render(request, 'success.html')
