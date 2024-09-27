from django.contrib import admin

from .models import Department, Role, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display=['tittle']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id', 'first_name', 'last_name', 'department', 'role', 
                  'email','phone_number', 'salary', 'joining_date']