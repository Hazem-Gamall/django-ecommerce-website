from django.http import HttpResponse
from django.shortcuts import render

from cart.models import Order

# Create your views here.
def index(request):
    orders = []
    user_orders_queryset = Order.objects.filter(user=request.user).order_by('-order_time')
    for order in user_orders_queryset:
        temp_order_dict = {}
        temp_order_dict['date'] = order.order_time
        temp_order_dict['products'] = order.products.all()
        orders.append(temp_order_dict) 
        
    return render(request, 'views/order_history.html', {'orders':orders})