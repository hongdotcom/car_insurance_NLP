from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .analysis import bing_search, nlp_check
from django import forms
from .forms import SearchForm
from django.core.paginator import Paginator
# Create your views here.

def home(request):
  if request.method == 'POST':
    form = SearchForm(request.POST)
    if form.is_valid():
      # print('call serach and iterate list')
      bing_res = bing_search(request.POST['searchTxt'])
      # nlp_res = True
      nlp_res = nlp_check(request.POST['searchTxt'])      
      # paginator = Paginator(list(bing_res), 10)
      # page_number = request.GET.get('page')
      # page_obj = paginator.get_page(page_number)
      # import moduleName from 'module'return render(request, 'home.html', {'form': form,'bing_res':bing_res,'nlp_res':nlp_res,'page_obj': page_obj})
      return render(request, 'home.html', {'form': form,'bing_res':bing_res,'nlp_res':nlp_res})
  else:
    form = SearchForm()
    return render(request, 'home.html', {'form': form})

def insurance(request):
  return render(request, 'insurance.html')

def auction(request):
  return render(request, 'auction.html')

def car_detail(request):
  return render(request, 'car_detail.html')