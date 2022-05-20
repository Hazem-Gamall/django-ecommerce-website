from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from cart.models import Order, ProductOrder

# Create your views here.
@login_required
def index(request):
    orders = []
    user_orders_queryset = Order.objects.filter(user=request.user).order_by('-order_time')
    # print(user_orders_queryset[0])

    for order in user_orders_queryset:
        temp_order_dict = {}
        temp_order_dict['date'] = order.order_time
        temp_order_dict['products'] = []
        for product in order.products.all():
            product_dict = {'product':product, 'quantity':ProductOrder.objects.get(order=order, products__id=product.id).quantity}
            temp_order_dict['products'].append(product_dict)
        orders.append(temp_order_dict) 
    # print(orders[0])    
    return render(request, 'views/order_history.html', {'orders':orders})