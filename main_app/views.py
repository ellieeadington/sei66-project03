from django.shortcuts import render,redirect
from .models import Cafe, CoffeeBean, User

# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import CreateView


class CafeCreate(CreateView):
  model = Cafe
  fields = '__all__'

  
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
  return render(request, 'coffee_beans/index.html', { 'coffee_beans': coffee_beans })


def coffee_beans_detail(request, coffee_beans_id):
  coffee_bean = CoffeeBean.objects.get(id = coffee_beans_id)
  return render(request, 'coffee_beans/detail.html',{ 'coffee_bean': coffee_bean })