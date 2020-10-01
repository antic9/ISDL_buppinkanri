"""
実際の動作を管理するファイル
"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm

import datetime
import pytz
import os, sys

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)

from .models import *
from . import forms
import config

CHANNEL_ID = 'G8XP0KUNQ'

# class Slack(object):
#   __slacker = None

#   def __init__(self, token):
#     self.__slacker = Slacker(token)

#   def post_to_channel(self, channel, message):
#     self.__slacker.chat.post_message(CHANNEL_ID, message)

# slack = Slack(config.slack_token)

def index(request):
  equipment_list = Equipment.objects.all()
  now = timezone.now()
  for j in equipment_list:
    print(j.timestamp <= now)
    if j.timestamp <= now:
      if j.state == 1:
        print("changed status")
        j.state = 0
        j.borrower=""
        j.remark=""
        j.save()
      elif j.state == 3:
        print("changed status")
        j.state = 2
        j.save()
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
    print(j.timestamp <= now)
    if j.timestamp <= now:
      if j.state == 1:
        print("changed status")
        j.state = 0
        j.borrower=""
        j.remark=""
        j.save()
      elif j.state == 3:
        print("changed status")
        j.state = 2
        j.save()
  context = {
    'equipment_list': equipment_list,
  }
  return render(request, 'equipments/approve.html', context)

def mylist(request):
  equipment_list1 = Equipment.objects.all()
  now = timezone.now()
  for j in equipment_list1:
    print(j.timestamp <= now)
    if j.timestamp <= now:
      if j.state == 1:
        print("changed status")
        j.state = 0
        j.borrower=""
        j.remark=""
        j.save()
      elif j.state == 3:
        print("changed status")
        j.state = 2
        j.save()
  userf = request.user.first_name
  userl = request.user.last_name
  username = userf+userl
  equipment_list = Equipment.objects.filter(borrower = username)
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
      # temp.timestamp = datetime.datetime.now()
      # print("!!!!!!"+temp.timestamp)
      temp.save()


    return HttpResponseRedirect(reverse('equipments:index'))

  if request.POST['action'] == 'returning':
    userf = request.user.first_name
    userl = request.user.last_name
    username = userf+userl
    if temp.borrower == username:
      if temp.state == 2:
          temp.state = 3
          now = datetime.datetime.now()
          now += datetime.timedelta(minutes=15)
          temp.timestamp = now
          temp.save()

    return HttpResponseRedirect(reverse('equipments:index'))

  # if request.POST['action'] == 'extension':
  #   if temp.borrower == request.POST['name']:
  #     temp.save()

  #   return HttpResponseRedirect(reverse('equipments:index'))
  return HttpResponseRedirect(reverse('equipments:index'))

def new(request):
  form = forms.NewForm()

  context = {
    'form': form,
  }

  return render(request, 'equipments/new.html', context)

def create(request):
  temp = Equipment(
    name=request.POST['name'],
    bunrui=request.POST['bunrui'],
    state=0,
    owner='',
    remark=request.POST['remark']
    )
  temp.save()

  return HttpResponseRedirect(reverse('equipments:index'))



class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/login.html'
