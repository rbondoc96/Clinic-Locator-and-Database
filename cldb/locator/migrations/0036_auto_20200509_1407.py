# Generated by Django 3.0.6 on 2020-05-09 21:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0035_auto_20200509_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='location',
            name='date_submitted',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date Submitted'),
            preserve_default=False,
        ),
    ]