# Generated by Django 3.0.5 on 2020-04-15 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0011_auto_20200412_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='website',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='LocationHistory',
        ),
    ]