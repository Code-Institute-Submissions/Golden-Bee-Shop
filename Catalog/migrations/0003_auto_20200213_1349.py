# Generated by Django 2.2.4 on 2020-02-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0002_auto_20200213_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Product Name'),
        ),
    ]
