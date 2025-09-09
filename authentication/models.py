from django.db import models

# Create your models here.
#Aqui aplicamos herencia 
    
class Country(models.Model):
    name =models.CharField(max_length =20)
    abrev = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

class Department(models.Model):
    name =models.CharField(max_length =20)
    abrev = models.CharField(max_length=5)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    
class City(models.Model):
    id_department = models.ForeignKey(Department,on_delete=models.CASCADE)
    name =models.CharField(max_length =20)
    abrev = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20,blank=True)
    mobile_phone = models.CharField(max_length=13)
    address =  models.CharField(max_length=100)
    email = models.CharField(max_length=45)
    password = models.TextField()
    id_city = models.ForeignKey(City,on_delete=models.CASCADE)
    status = models.BooleanField (default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)  
