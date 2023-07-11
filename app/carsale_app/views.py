from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Car, Account
from .forms import CarSellForm
from django.contrib.auth.forms import UserCreationForm

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
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']

            # Save the data in the Car dataset
            car = Car(make=make, model=model, price=price, image=image)
            car.save()
            form.save()
            return redirect('catalog')
    else:
        form = CarSellForm()
 
    return render(request, 'sell_car.html', {'form': form})
