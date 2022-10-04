from django.shortcuts import render,redirect
from .models import Cafe, CoffeeBean, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .filters import CoffeeBeanFilter
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms


class CafeCreate(CreateView):
  model = Cafe
  fields = ['cafe_name','date_founded','address_line_1', 'address_line_2','address_city', 'address_county', 'address_country', 'address_postcode']

  #Overriding
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CafeUpdate(UpdateView):
  model = Cafe
  fields = '__all__'
  
class CafeDelete(DeleteView):
  model = Cafe
  success_url = '/cafes/'


# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def cafes_index(request):
  cafes = Cafe.objects.all()
  return render(request, 'cafes/index.html', { 'cafes': cafes })

# ROB SECTION



def cafes_detail(request, cafe_id):

  cafe = Cafe.objects.get(id = cafe_id)
  
  return render(request, 'cafes/detail.html', {'cafe': cafe})

















# ASHISH SECTION
def signup(request):
  error_message = ""
  if request.method =="POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
          user = form.save()
          login(request, user) 
          return redirect('index') 
      else:
          error_message = "Invalid signup - please try again later"

  form = UserCreationForm 
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)





















# ELLIE SECTION

def coffee_beans_index(request):
  coffee_beans = CoffeeBean.objects.all()
  coffee_bean_filter = CoffeeBeanFilter(request.GET, queryset=coffee_beans)
  coffee_beans = coffee_bean_filter.qs
  context = {
    'coffee_bean_filter': coffee_bean_filter,
    'coffee_beans': coffee_beans
  }
  return render(request, 'coffee_beans/index.html', context )


def coffee_beans_detail(request, coffee_beans_id):
  coffee_bean = CoffeeBean.objects.get(id = coffee_beans_id)
  cafes = Cafe.objects.filter(coffee_beans = coffee_bean)

  return render(request, 'coffee_beans/detail.html',{ 'coffee_bean': coffee_bean, 'cafes': cafes})

def cafe_owner_profile(request, cafe_id):
  cafe = Cafe.objects.get(id = cafe_id)
  return render(request, 'users/profile/cafe_profile.html',{'cafe': cafe})

def coffee_bean_create(request, cafe_id):
  cafe = Cafe.objects.get(id = cafe_id)
  coffee_beans = CoffeeBean.objects.filter(cafe = cafe)
  return render(request,'users/profile/update/coffee_beans.html', {'cafe': cafe, 'coffee_beans': coffee_beans} )

