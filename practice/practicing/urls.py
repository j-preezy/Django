from django.urls import path
from practicing import views
urlpatterns = [
    path('',views.index),
    path('about/',views.about)

]