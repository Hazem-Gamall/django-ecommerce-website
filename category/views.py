from itertools import product
from django.shortcuts import render
from category.models import Category
from product.models import Brand
from django.core.paginator import Paginator
# Create your views here.

def index(request, id):
    price_filter = request.GET.get('price-filter', 'price')
    brands_filter = request.GET.getlist('brand', [])
    requested_page = request.GET.get('page', '')
    
    required_category = Category.objects.get(id = id)
    if brands_filter:
        products = required_category.products.filter(brand__name__in=brands_filter).order_by(price_filter)
    else:
        products = required_category.products.order_by(price_filter)

    paginator = Paginator(products, 6)
    if requested_page:
        requested_page = int(requested_page)
        products = paginator.page(requested_page)
    else:
        products = paginator.page(1)
        requested_page = 1
    return render(request, 'views/products_display.html', {'requested_page':requested_page,'page_range':paginator.page_range,'section_title': required_category.name, 'products':products, 'checked':'min' if price_filter == 'price' else 'max', 'brands':Brand.objects.all(), 'selected_brands':brands_filter})