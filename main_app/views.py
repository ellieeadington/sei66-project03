from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BrewingMethod, Cafe, CoffeeBean, User, Event
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .forms import BrewingMethodForm, CoffeeBeanForm, ReviewForm, EventForm
from .filters import CoffeeBeanFilter, CafeFilter
from django.urls import reverse_lazy


#@allowed_users(allowed_roles=['Cafe Owner'])
class CafeCreate(LoginRequiredMixin, CreateView):
  model = Cafe
  fields = ['cafe_name','date_founded','address_line_1', 'address_line_2','address_city', 'address_county', 'address_country', 'address_postcode']

  #Overriding
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CafeUpdate(LoginRequiredMixin, UpdateView):
  model = Cafe
  fields = '__all__'
  
class CafeDelete(LoginRequiredMixin, DeleteView):
  model = Cafe
  success_url = '/cafes/'


# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def cafes_index(request):
  cafes = Cafe.objects.all()
  cafe_filter = CafeFilter(request.GET, queryset=cafes)
  cafes = cafe_filter.qs
  context = {
    'cafe_filter': cafe_filter,
    'cafes': cafes
  }
  return render(request, 'cafes/index.html', context)

# ROB SECTION

def cafes_detail(request, cafe_id):

  cafe = Cafe.objects.get(id = cafe_id)
  
  brewing_method_form = BrewingMethodForm()
  event_form = EventForm()
  return render(request, 'cafes/detail.html', {'cafe': cafe, 'brewing_method_form': brewing_method_form, 'event_form': event_form})



def add_brewing_method(request, cafe_id):

  form = BrewingMethodForm(request.POST)

  if form.is_valid():
    new_brewing_method = form.save(commit=False)
    new_brewing_method.cafe_id = cafe_id
    new_brewing_method.save()
    return redirect('brewing_method_edit', cafe_id=cafe_id)   
  


def brewing_method_edit(request, cafe_id):
  cafe = Cafe.objects.get(id = cafe_id)
  print(cafe)
  brewing_methods = BrewingMethod.objects.filter(cafe = cafe)
  brewing_method_form = BrewingMethodForm()
  return render(request,'users/profile/update/brewing_methods.html', {'cafe': cafe, 'brewing_methods': brewing_methods, 'brewing_method_form': brewing_method_form } )


def add_event(request, cafe_id):

  form = EventForm(request.POST)

  if form.is_valid():
    new_event = form.save(commit=False)
    new_event.cafe_id = cafe_id
    new_event.save()
  return redirect('event_edit', cafe_id = cafe_id)

def event_edit(request, cafe_id):
  cafe = Cafe.objects.get(id = cafe_id)
  print(cafe)
  events = Event.objects.filter(cafe = cafe)
  event_form = EventForm()
  return render(request,'users/profile/update/events.html', {'cafe': cafe, 'events': events, 'event_form': event_form } )















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
  # is_cafe_owner = request.user.profile.profile_type_set.all()
  # print('is cafe owner:', is_cafe_owner)

  cafe = Cafe.objects.get(id = cafe_id)
  return render(request, 'users/profile/cafe_profile.html',{'cafe': cafe })

def coffee_bean_edit(request, cafe_id):
  cafe = Cafe.objects.get(id = cafe_id)
  print(cafe)
  coffee_beans = CoffeeBean.objects.filter(cafe = cafe)
  coffee_bean_form = CoffeeBeanForm()
  return render(request,'users/profile/update/coffee_beans.html', {'cafe': cafe, 'coffee_beans': coffee_beans, 'coffee_bean_form': coffee_bean_form } )

def add_coffee_bean(request, cafe_id):
    coffee_bean_form = CoffeeBeanForm(request.POST) 
    cafe = Cafe.objects.get(id = cafe_id)
    if coffee_bean_form.is_valid():
        new_coffee_bean = coffee_bean_form.save(commit=False) 
        new_coffee_bean.cafe_id = cafe_id
        new_coffee_bean.save()
        new_beans_id = []
        new_beans_id.append(new_coffee_bean.pk)
        # 21 , 4
        cafe.coffee_beans.set(new_beans_id)

    return redirect('coffee_bean_edit', cafe_id=cafe_id)   
  
class CoffeeBeanUpdate(UpdateView):
    model = CoffeeBean
    fields = '__all__'
    
class CoffeeBeanDelete(DeleteView):
  model = CoffeeBean
  success_url = '/profile/cafe/<int:cafe_id>/coffee_beans/'  
  
  def get_success_url(self):
      return reverse_lazy('coffee_bean_edit', kwargs={'cafe_id': self.object.pk})
    
def add_review(request, cafe_id):  
    
    form = ReviewForm(request.POST)
    
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.cafe_id = cafe_id
        new_review.save()
    return redirect('detail', cafe_id = cafe_id)     