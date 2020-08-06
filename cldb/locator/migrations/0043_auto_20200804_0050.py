# Generated by Django 3.0.8 on 2020-08-04 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0042_auto_20200803_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Review Type')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='review_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locator.ReviewType'),
        ),
    ]
