from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from product.models import Brand, Product
from product.models import Category
# from home.models import Product

# Create your views here.




def index(request):
    
    offers = Product.objects.all()
    

    template = loader.get_template('views/home.html')
    return render(request, 'views/home.html', {'products':offers, 'section_title':'Best offers!', 'categories':Category.objects.all()})

def search(request):
    product = request.GET.get('product')
    category = request.GET.get('category')
    print(category)
    price_filter = request.GET.get('price-filter', 'price')
    brands_filter = request.GET.getlist('brand', [])
    
    if category == 'all':
        products = Product.objects.filter(name__icontains=product)    
    else:
        products = Product.objects.filter(name__icontains=product, category__name=category)

    if brands_filter:
        products = products.filter(brand__name__in=brands_filter).order_by(price_filter)
    else:
        products = products.filter().order_by(price_filter)       
    return render(request, 'views/products_display.html', {'products':products, 'section_title':product,'categories':Category.objects.all(), 'brands':Brand.objects.all(), 'checked':'min' if price_filter == 'price' else 'max', 'selected_brands':brands_filter})

