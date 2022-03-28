from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

User = settings.AUTH_USER_MODEL

class Product(models.Model):

    class Unit(models.TextChoices):
        Dollar = '$'
        Euro = '£'
        Turkish_Lira = 'TL'

    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    currency = models.CharField(max_length=2, choices=Unit.choices, default=Unit.Turkish_Lira)
    product_description = models.TextField()
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product_detail',args=[str(self.id)])


class Comment(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='comments')
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('product_list')