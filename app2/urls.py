from django.urls import path
from app1.views import *
app_name='app2'
urlpatterns=[
    path('app2_function/',app2_function,name='app2_function1'),
]