# Generated by Django 2.0.3 on 2018-06-17 18:24

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=100, verbose_name='First name')),
                ('lname', models.CharField(blank=True, max_length=100, verbose_name='Last name')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Postal address')),
                ('telephone', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True, verbose_name='Is active')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('ASSIGNED', 'ASSIGNED'), ('FINISHED', 'FINISHED'), ('CLOSED', 'CLOSED')], default='NEW', max_length=256)),
                ('table', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(15)])),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 6, 17, 18, 24, 33, 788571))),
                ('due_date', models.DateTimeField(default=datetime.datetime(2018, 6, 17, 18, 54, 33, 788571))),
                ('assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to='oms.Employee', verbose_name='Assigned to')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(max_length=512)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('active', models.BooleanField()),
                ('quantity', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 6, 17, 18, 24, 33, 772946))),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='oms.Product'),
        ),
    ]
