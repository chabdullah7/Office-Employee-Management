from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Role(models.Model):
    tittle=models.CharField(max_length=100)
    def __str__(self):
        return self.tittle
    
class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    department=models.ForeignKey(Department, on_delete=models.CASCADE, blank=False)
    role=models.ForeignKey(Role, on_delete=models.CASCADE, blank=False,)
    email=models.EmailField(blank=False, unique=True)
    phone_number=models.IntegerField(blank=False, unique=True)
    salary=models.IntegerField(null=False)
    joining_date=models.DateField(blank=False)

    
    

