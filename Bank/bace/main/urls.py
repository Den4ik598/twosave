from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index1, name='Table'),
    path('report',views.report, name='Report'),
    path('database/',views.Data_people, name='database'),
    path('add_People',views.add_People, name = "add_People"),
    path('delete',views.function, name= 'delete'),
    path('ex',views.ex, name= 'ex'),
]

