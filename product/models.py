from django.db import models
from category.models import Category
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f'id:{self.id}\nname:{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'id:{self.id}\nname: {self.name}\ndescription: {self.description}\nprice: {self.price}\nbrand: {self.brand}\nimage: {self.image}\ncategory: {self.category}'
    

