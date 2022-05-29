from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description','brand', 'category','price', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['description'].widget.attrs['class']='form-control'
        self.fields['description'].widget.attrs['rows']='5'
        self.fields['brand'].widget.attrs['class']='form-control'
        self.fields['category'].widget.attrs['class']='form-control'
        self.fields['price'].widget.attrs['class']='form-control'
        self.fields['image'].widget.attrs['class']='form-control'
        self.fields['image'].widget.attrs['rows']='2'
