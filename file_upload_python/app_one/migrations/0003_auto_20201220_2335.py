# Generated by Django 2.2.4 on 2020-12-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_auto_20201220_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
