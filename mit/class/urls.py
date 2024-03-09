from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('schools/', views.schools, name='school'),
    path('insertstudents/', views.insertstudents, name='insertstudents')



]