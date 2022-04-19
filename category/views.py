from django.shortcuts import render
from category.models import Category
from product.models import Brand, Product
# Create your views here.

def index(request, id):
    price_filter = request.GET.get('price-filter', 'price')
    brands_filter = request.GET.getlist('brand', [])
    
    required_category = Category.objects.get(id = id)
    if brands_filter:
        products = Product.objects.filter(category=required_category, brand__name__in=brands_filter).order_by(price_filter)
    else:
        products = Product.objects.filter(category=required_category).order_by(price_filter)       
    return render(request, 'views/products_display.html', {'section_title': required_category.name, 'products':products, 'checked':'min' if price_filter == 'price' else 'max', 'brands':Brand.objects.all(), 'selected_brands':brands_filter})