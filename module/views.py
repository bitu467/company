from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Dept, Employee

# Create your views here.


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