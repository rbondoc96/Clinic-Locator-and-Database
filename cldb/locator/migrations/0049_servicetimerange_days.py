# Generated by Django 3.0.8 on 2020-08-05 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0048_auto_20200805_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetimerange',
            name='days',
            field=models.ManyToManyField(blank=True, null=True, to='locator.Day', verbose_name='Days Offered'),
        ),
    ]