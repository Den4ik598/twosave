from django.urls import path
from . import views

app_name= 'database'

urlpatterns = [
    path('',views.NumberFormView.as_view(), name='database'),
    path('database/', views.apply_people, name='apply_people'),
]

