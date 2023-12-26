from django.db import models
from django.contrib.auth.models import User

from product.models import ProductModel


class LikeModel(models.Model):
    pro_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

