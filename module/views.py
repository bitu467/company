from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Dept, Employee

# Create your views here.


def saveEmp(request):
    if request.method == "POST":
        ECode = request.POST['ECode']
        Name = request.POST['name']
        DOB = request.POST['dob']
        department = request.POST['dept']
        salary = request.POST['salary']
        emp = Employee(ECode=ECode, Name=Name, DOB=DOB,
                       Dept=department, salary=salary)
        emp.save()
    output = "Employee created"
    return render(request, 'module.html', {'output': output})


def delete_checked(request):
    if request.method == "POST":
        selected_item_ids = request.POST.getlist('selected_items')
        selected_item_ids = [int(x) for x in selected_item_ids]
        Dept.objects.filter(ID__in=selected_item_ids).delete()
    output = "Department Deleted"
    return render(request, 'module.html', {'output': output})


def saveDept(request):
    output = ''
    if request.method == 'POST':
        code = request.POST['code']
        name = request.POST['name']
        dept = Dept(Code=code, Name=name)
        dept.save()
        output = "Department created"
    return render(request, 'module.html', {'output': output})


def module(request):
    template = loader.get_template('module.html')
    # new added
    dept = Dept.objects.all().values()
    emp_list = Dept.objects.all().values()
    context = {
        'dept': dept,
        'emp_list': emp_list
    }
    return HttpResponse(template.render(context, request))


def department(request):
    dept = Dept.objects.all().values
    template = loader.get_template('dept.html')
    context = {
        'dept': dept
    }
    return HttpResponse(template.render(context, request))


def employee(request):
    emp_list = Employee.objects.all().values()
    template = loader.get_template('employee.html')
    context = {
        'emp_list': emp_list
    }
    return HttpResponse(template.render(context, request))
