# Generated by Django 2.0.3 on 2018-03-23 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_added',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
