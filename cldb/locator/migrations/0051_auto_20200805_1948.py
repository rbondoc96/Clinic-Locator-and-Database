# Generated by Django 3.0.8 on 2020-08-06 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0050_delete_bookmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authmethod',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='auth_method_list',
            field=models.ManyToManyField(blank=True, to='locator.AuthMethod', verbose_name='Authorization Methods Accepted'),
        ),
        migrations.AlterField(
            model_name='location',
            name='ccf_category_list',
            field=models.ManyToManyField(blank=True, to='locator.CcfCategory', verbose_name='UDS Chain of Custody Forms Accepted'),
        ),
        migrations.AlterField(
            model_name='servicetimerange',
            name='days',
            field=models.ManyToManyField(blank=True, to='locator.Day', verbose_name='Days Offered'),
        ),
    ]
