from django.shortcuts import render
from product.models import Brand, Product
from django.core.paginator import Paginator

# Create your views here.
def search(request):
    product = request.GET.get('product')
    category = request.GET.get('category')
    requested_page = request.GET.get('page', '')

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

    paginator = Paginator(products, 6)
    
    if requested_page:
        requested_page = int(requested_page)
        products = paginator.page(requested_page)
    else:
        products = paginator.page(1)
        requested_page = 1       
    return render(request, 'views/products_display.html', {'requested_page':requested_page,'page_range':paginator.page_range,'products':products, 'section_title':product, 'brands':Brand.objects.all(), 'checked':'min' if price_filter == 'price' else 'max', 'selected_brands':brands_filter})

