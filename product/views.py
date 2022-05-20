from django.shortcuts import render
from product.models import Product
from django.http import JsonResponse
# Create your views here.
def index(request, id):
    product = Product.objects.get(id = id)
    print(product)
    return render(request, 'views/product.html', {'product':product})

def api_product(request, id):
    product = Product.objects.get(id = id)
    product_dict = {
        'id':product.id,
        'name':product.name,
        'description':product.description,
        'price':product.price,
        'brand':product.brand.name,
        'image':product.image,
        'category': product.category.name
    }
    print(product_dict)
    return JsonResponse(product_dict)