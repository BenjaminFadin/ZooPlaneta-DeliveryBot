from django.db import models
from shared.models import BaseModel


class Category(BaseModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children')
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    unit_price = models.CharField(max_length=15)
    inventory = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Order(BaseModel):
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETE = "C"
    PAYMENT_STATUS_FAILED = "F"
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed"),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey('users.User', on_delete=models.PROTECT)
    # ichidan reverse related objectni chaqirish uchun bu yerda order.orderitem_set.quantity deb olinadi.
    # related name bilan order.items


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.CharField(max_length=20)


class Courier(BaseModel):
    pass
