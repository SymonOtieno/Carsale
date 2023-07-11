from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, name, password):
        user = self.model(name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password):
        user = self.create_user(name=name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    def register_user(self, name, password):
        user = self.create_user(name=name, password=password)
        return user

class Account(AbstractBaseUser):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'

    objects = AccountManager()

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.CharField(max_length=100, default='')
    # Add more fields as needed (e.g., body style, mileage, etc.)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
    
class BillingInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    payment = models.CharField(max_length=50)
    car_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
