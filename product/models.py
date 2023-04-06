from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_name

class Review(models.Model):
    text = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} ---> {self.product}'
