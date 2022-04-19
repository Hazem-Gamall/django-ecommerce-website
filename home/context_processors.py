from category.models import Category

def category_context(request):
    return {'categories':Category.objects.all()}