# Generated by Django 3.0.8 on 2020-08-05 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0044_auto_20200804_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='date_submitted',
            new_name='date_created',
        ),
    ]
