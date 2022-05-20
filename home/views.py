from django.shortcuts import render
from product.models import Product
# from home.models import Product

# Create your views here.




def index(request):
    
    offers = Product.objects.all()

    return render(request, 'views/home.html', {'products':offers[:3], 'section_title':'Best offers!'})

