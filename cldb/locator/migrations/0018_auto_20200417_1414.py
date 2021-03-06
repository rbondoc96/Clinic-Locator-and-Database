# Generated by Django 3.0.5 on 2020-04-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0017_auto_20200417_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='auth_method_list',
            field=models.ManyToManyField(to='locator.AuthMethod', verbose_name='Authorization Methods Accepted'),
        ),
        migrations.AlterField(
            model_name='location',
            name='ccf_category_list',
            field=models.ManyToManyField(to='locator.CcfCategory', verbose_name='Chain of Custody Forms Accepted'),
        ),
    ]
