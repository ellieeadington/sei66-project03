from django.shortcuts import render
from .models import Cafe, CoffeeBean

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def cafes_index(request):
  cafes = Cafe.objects.all()
  return render(request, 'cafes/index.html', { 'cafes': cafes })

# ROB SECTION


















# ASHISH SECTION





















# ELLIE SECTION

def coffee_beans_index(request):
  coffee_beans = CoffeeBean.objects.all()
  return render(request, 'coffee_beans/index.html', { 'coffee_beans': coffee_beans })


def coffee_beans_detail(request, coffee_beans_id):
  coffee_bean = CoffeeBean.objects.get(id = coffee_beans_id)
  return render(request, 'coffee_beans/detail.html',{ 'coffee_bean': coffee_bean })