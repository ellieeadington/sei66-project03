from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BrewingMethod, Cafe, CoffeeBean, Event
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BrewingMethodForm, CoffeeBeanForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ReviewForm, EventForm
from django import forms
from .forms import BrewingMethodForm, CoffeeBeanForm, ReviewForm, EventForm
from .filters import CoffeeBeanFilter, CafeFilter
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
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
  user = User.objects.get(pk=request.user.pk)
  user_profile = user.profile
  print(user_profile.__str__())
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
  review_form = ReviewForm()
  return render(request, 'cafes/detail.html', {'cafe': cafe, 'brewing_method_form': brewing_method_form, 'event_form': event_form, 'review_form': review_form})



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
      form = UserRegisterForm(request.POST)
      if form.is_valid():
          user = form.save()
          login(request, user)
          messages.success(request, 'Your account has been created!')
          return redirect('profile') 
      else:
          error_message = "Invalid signup - please try again later"

  form = UserRegisterForm 
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def profile(request):
    if request.method =="POST":
      u_form = UserUpdateForm(request.POST, instance=request.user)
      p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

      if p_form['is_cafe_owner']:
        p_form.save()
        print("p_form is valid")
        # return redirect('profile_cafeowner')
        return HttpResponse("profile_user")
      if u_form.is_valid():
        u_form.save()
        print("u_form is valid")
        return HttpResponse("user_account_updated")

    else:
      u_form = UserUpdateForm(instance=request.user)
      p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
      'u_form': u_form, 
      'p_form': p_form
    }
    return render(request, 'users/profile/profile.html', context)


# def profile_cafeowner(request):
#   user = User.objects.get(pk=request.user.pk)
#   user_profile = user.profile
#   print(user.profile.is_cafe_owner)
 
#   return render(request, 'users/profile/cafe_profile.html')



# ELLIE SECTION
def cafe_owner_profile(request, cafe_id):
  cafe = Cafe.objects.get(id = cafe_id)
  return render(request, 'users/profile/cafe_profile.html',{'cafe': cafe })


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