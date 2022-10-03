from django.shortcuts import render
from .models import Cafe

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





















# ELLIE SECTION