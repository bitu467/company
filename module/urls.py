from django.urls import path
from . import views

urlpatterns = [
    path('module/', views.module, name='module'),
    path('department/', views.department, name='department'),
    path('employee/', views.employee, name='employee'),
    path('saveDept', views.saveDept, name='saveDept')

]
