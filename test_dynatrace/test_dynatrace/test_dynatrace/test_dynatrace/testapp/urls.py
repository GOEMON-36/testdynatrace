from django.urls import path
from . import views
from .views import *

app_name = 'testapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('result/', result, name='result')
]