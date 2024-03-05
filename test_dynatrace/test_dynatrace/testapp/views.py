from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect#, get_object_or_404a
from django.views.generic import View, TemplateView, CreateView, ListView, DetailView, FormView
#from .forms import *
from django import forms
from django.apps import apps

from django.http import HttpResponseRedirect, HttpResponseBadRequest
import datetime
import random


class HomeView(TemplateView):
  template_name = 'home.html'

def result(request):
  if request.method == "POST":
    
    #リクエストデータ取得
    print(request.POST)
    selected_car = request.POST.get('selected_car')

    # 操作するテーブル名指定　テーブルは固定
    table = 'Car'

    #実際に操作するデータベース、テーブルと連携
    db = apps.get_model('testapp', table) 

    #
    car_data = db.objects.filter(car=selected_car)
    print(car_data)

    '''
    car_data = [
        {'prime': '100000', 'dealership': '200.00'},
        {'prime': '200000', 'dealership': '150.00'},
        {'prime': '5000', 'dealership': '300.00'}
    ]
    '''
    return render(request, 'result.html', {
      'car_data':car_data,
      })



