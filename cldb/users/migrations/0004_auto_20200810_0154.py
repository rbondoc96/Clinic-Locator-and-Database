# Generated by Django 3.0.8 on 2020-08-10 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200809_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertype',
            options={'verbose_name': 'User Type'},
        ),
    ]