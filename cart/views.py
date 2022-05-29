from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from cart.models import Order
from product.models import Product

@login_required
def index(request):
    return render(request, 'views/cart.html')

# @login_required   
def checkout(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            print(request.POST)
            order = Order(user=request.user)
            order.save()
            id_list = request.POST.getlist('id')
            print(id_list)
            for str_dict in id_list:
                #str_dict = '9,1'
                cart_item_list = str_dict.split(',')#['9','1']
                product_id = cart_item_list[0]
                product_quantity = cart_item_list[1]
                print(product_id, product_quantity)
                order.products.add(Product.objects.get(id=product_id), through_defaults={'quantity':product_quantity})
                
            
            
            # print(order)
            messages.success(request, 'Order created successfully')
            return redirect('/')
        else:
            messages.error(request, "Error order can't be empty", extra_tags='danger')
            return redirect('/')

    return HttpResponse('error')