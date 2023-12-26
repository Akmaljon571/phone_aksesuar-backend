from django.db import models
from django.contrib.auth.models import User

from product.models import ProductModel


class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s order for {self.product.title} (Count: {self.count})"
