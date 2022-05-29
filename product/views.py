from django.shortcuts import render, redirect, HttpResponse
from product.models import Product, Brand
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.
def index(request, id):
    product = Product.objects.get(id = id)
    print(product)
    return render(request, 'views/product.html', {'product':product, 'brands':Brand.objects.all()})

def read_product(request, id):
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

def update_product(request, id):
    if request.method == "POST":
        new_data = request.POST
        Product.objects.filter(id = id).update(
            name = new_data['name'],
            description = new_data['description'],
            price = new_data['price'],
            brand_id = new_data['brand']
            )
        messages.success(request, 'Product updated successfuly')
        return redirect('product-url', id=id)
    else:
        return HttpResponse("error")

def delete_product(request, id):
    Product.objects.get(id=id).delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('/')
    