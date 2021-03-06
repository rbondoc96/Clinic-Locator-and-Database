# Generated by Django 3.0.5 on 2020-04-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0005_auto_20200412_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='comments',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AddConstraint(
            model_name='location',
            constraint=models.UniqueConstraint(fields=('name', 'branch_name'), name='location_name_branch_name_key'),
        ),
    ]
