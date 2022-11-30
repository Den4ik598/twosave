from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index1, name='Table'),
    path('report',views.report, name='Report'),
]

