from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

from .models import Employee, Role, Department
from .forms import EmployeeForm
from datetime import datetime
from django.utils.dateparse import parse_date


def home(request):
    return render(request, 'home.html')


def view_emp(request):
    emp=Employee.objects.all()

    context={
        'emp' : emp
    }

    return render(request,'view_emp.html',context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        role = request.POST.get('role')
        email = request.POST.get('email')
        phone_number = int(request.POST.get('phone_number'))
        salary = int(request.POST.get('salary'))
        joining_date = request.POST.get('joining_date')
        
        department, _ = Department.objects.get_or_create(name=department)
        role, _ = Role.objects.get_or_create(tittle=role)
        
        new_emp = Employee(
                           first_name = first_name, 
                           last_name = last_name,
                           department = department,
                           role = role,
                           email = email,
                           phone_number = phone_number,
                           salary = salary,
                           joining_date = joining_date
        )

        new_emp.save()

        return HttpResponse("Employee Add Successfully")
   
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    
    else:
        return HttpResponse("Exception Error Occured! Employee Has Not Been Added")  
    

def filter_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        role = request.POST.get('role')

        emp=Employee.objects.all()

        if first_name:
            emp = emp.filter(first_name__icontains=first_name)

        if last_name:
            emp = emp.filter(last_name__icontains=last_name)

        if department:
           emp= emp.filter(department__name__icontains = department)

        if role:
           emp= emp.filter(role__tittle__icontains = role)
        
        context={
            'emp' : emp
        }

        return render(request, 'view_emp.html', context)
    
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    
    else:
        return HttpResponse("An Exception Occoured")
    

def remove_emp(request, emp_id=None):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        if emp_id:
            try:
                Employee.objects.get(id=emp_id).delete()
                return HttpResponse("Employee Removed Successfully")
            except Employee.DoesNotExist:
                return HttpResponse("Employee with the given ID does not exist")

    emp = Employee.objects.all()
    return render(request, 'remove_emp.html', {'emp': emp})


def update_emp(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if 'search' in request.POST:
            # Handle Search
            emp = Employee.objects.filter(id=employee_id).first() if employee_id else \
                  Employee.objects.filter(first_name__icontains=first_name, last_name__icontains=last_name).first()

            if emp:
                return render(request, 'update_emp.html', {'emp': emp})
            return HttpResponse("No employee found")

        elif 'update' in request.POST and employee_id:
            # Handle Update
            emp = get_object_or_404(Employee, id=employee_id)
            department = Department.objects.filter(name=request.POST.get('department')).first()
            role = Role.objects.filter(tittle=request.POST.get('role')).first()

            if not department or not role:
                return HttpResponse("Department or Role not found")

            # Update employee fields
            emp.first_name = first_name
            emp.last_name = last_name
            emp.department = department
            emp.role = role
            emp.email = request.POST.get('email')
            emp.phone_number = request.POST.get('phone_number')
            emp.salary = request.POST.get('salary')
            emp.joining_date = request.POST.get('joining_date')
            emp.save()
            return HttpResponse("Employee updated successfully")

    return render(request, 'update_emp.html')