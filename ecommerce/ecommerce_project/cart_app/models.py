from django.db import models

from shop_app.models import Product
# Create your models here.

class Cart(models.Model):
    objects = None
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)

class Cart_Items(models.Model):
    objects = None
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Cart_Items'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)
