from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=512)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField()
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(default=datetime.now())
    modified_date = models.DateTimeField(auto_now=True)
    # picturemaybe?

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('oms:product_detail',kwargs={'pk':self.pk})

class Order (models.Model):
    STATUS_CHOICES = (
    ('NEW','NEW'),
    ('ASSIGNED','ASSIGNED'),
    ('FINISHED','FINISHED'),
    ('CLOSED','CLOSED'),
    )

    Status = models.CharField(
        max_length=256,
        choices=STATUS_CHOICES,
        default='NEW',
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='products')
    table = models.PositiveIntegerField(validators=[MaxValueValidator(15),])
    timestamp = models.DateTimeField(default=datetime.now())
    due_date = due_date = models.DateTimeField(default=datetime.now()+timedelta(minutes=30))

    def __str__(self):
        return 'Order #' + str(self.id)

    def get_absolute_url(self):
        return reverse('oms:order_detail',kwargs={'pk':self.pk})
