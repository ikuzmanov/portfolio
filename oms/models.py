from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone

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

class Employee(models.Model):
    fname = models.CharField(blank=True, max_length=100, verbose_name='First name')
    lname = models.CharField(blank=True, max_length=100, verbose_name='Last name')
    country = CountryField()
    address = models.CharField(blank=True, max_length=100, verbose_name='Postal address')
    telephone = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name='Is active')

    def __str__(self):
        return self.fname +' '+ self.lname

    def get_absolute_url(self):
        return reverse('oms:employee_detail',kwargs={'pk':self.pk})

class Order (models.Model):
    STATUS_CHOICES = (
    ('NEW','NEW'),
    ('ASSIGNED','ASSIGNED'),
    ('FINISHED','FINISHED'),
    ('CLOSED','CLOSED'),
    )

    assigned = models.ForeignKey(Employee,on_delete=models.CASCADE, related_name='assigned', verbose_name='Assigned to')
    status = models.CharField(
        max_length=256,
        choices=STATUS_CHOICES,
        default='NEW',
    )
    total = models.DecimalField(max_digits=5, decimal_places=2)
    product = models.ManyToManyField(Product)
    table = models.PositiveIntegerField(validators=[MaxValueValidator(15),])
    timestamp = models.DateTimeField(default=timezone.now())
    due_date = models.DateTimeField(default=timezone.now()+timedelta(minutes=30))
    
    @property
    def total(self):
        result = self.product.aggregate(Sum('price'))
        return result['price__sum']

    def __str__(self):
        return 'Order #' + str(self.id)

    def get_absolute_url(self):
        return reverse('oms:order_detail',kwargs={'pk':self.pk})
