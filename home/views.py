from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from product.models import Brand, Product
from product.models import Category
from django.core.paginator import Paginator
# from home.models import Product

# Create your views here.




def index(request):
    
    offers = Product.objects.all()

    return render(request, 'views/home.html', {'products':offers[:3], 'section_title':'Best offers!'})

