from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm

#from selenium import webdriver

# from slacker import Slacker

import datetime
import pytz
import os, sys

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)

from .models import *
from . import forms
import config

CHANNEL_ID = 'G8XP0KUNQ'

def index(request):
  equipment_list = Equipment.objects.all()
  now = timezone.now()
  for j in equipment_list:
    if j.timestamp <= now:
      if j.state == 1:
        j.state = 0
      elif j.state == 3:
        j.state = 2
  context = {
    'equipment_list': equipment_list,
  }
  
  return render(request, 'equipments/index.html', context)

def detail(request, equipment_id):
  equipment = get_object_or_404(Equipment, pk=equipment_id)
  form = forms.BorrowForm()

  context = {
    'equipment': equipment,
    'form': form,
  }
  return render(request, 'equipments/detail.html', context)

def approval(request):
  equipment_list = Equipment.objects.all()
  now = timezone.now()
  for j in equipment_list:
    if j.timestamp <= now:
      if j.state == 1:
        j.state = 0
      elif j.state == 3:
        j.state = 2
  context = {
    'equipment_list': equipment_list,
  }
  return render(request, 'equipments/approve.html', context)

def mylist(request):
  userf = request.user.first_name
  userl = request.user.last_name
  username = userf+userl
  equipment_list = Equipment.objects.filter(borrower = username)
  now = timezone.now()
  for j in equipment_list:
    if j.timestamp <= now:
      if j.state == 1:
        j.state = 0
        j.borrower=""
        j.remark=""
      elif j.state == 3:
        j.state = 2
  context = {
    'equipment_list': equipment_list,
  }
  return render(request, 'equipments/mylist.html', context)

def approve(request, equipment_id):
  temp = Equipment.objects.get(pk=equipment_id)  
  temp.state = 2
  temp.save()
  #driver.refresh()
  return HttpResponseRedirect(reverse('equipments:approval'))

def returngoods(request, equipment_id):
  temp = Equipment.objects.get(pk=equipment_id)  
  temp.state = 0
  temp.borrower=""
  temp.remark=""
  temp.save()
  #driver.refresh()
  return HttpResponseRedirect(reverse('equipments:approval'))

def act(request, equipment_id):
  temp = Equipment.objects.get(pk=equipment_id)

  if request.POST['action'] == 'borrowing':
    if temp.state == 0:
      temp.state = 1
      temp.remark = request.POST['name']
      userf = request.user.first_name
      userl = request.user.last_name
      username = userf+userl
      temp.borrower = username
      now = datetime.datetime.now()
      now += datetime.timedelta(minutes=15)
      temp.timestamp = now
      temp.save()


    return HttpResponseRedirect(reverse('equipments:index'))

  if request.POST['action'] == 'returning':
    userf = request.user.first_name
    userl = request.user.last_name
    username = userf+userl
    if temp.borrower == username:
      temp.state = 3
      now = datetime.datetime.now()
      now += datetime.timedelta(minutes=15)
      temp.timestamp = now
      temp.save()

    return HttpResponseRedirect(reverse('equipments:index'))
  return HttpResponseRedirect(reverse('equipments:index'))

def new(request):
  form = forms.NewForm()

  context = {
    'form': form,
  }

  return render(request, 'equipments/new.html', context)



class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/login.html'
