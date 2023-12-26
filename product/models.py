from django.db import models

from category.models import CategoryModel


class ProductModel(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    cat_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
