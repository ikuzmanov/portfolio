# Generated by Django 2.0.3 on 2018-03-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20180324_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.CharField(max_length=40),
        ),
    ]
