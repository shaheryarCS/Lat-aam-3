# Generated by Django 3.0.4 on 2020-04-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_auto_20200426_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='customer',
            field=models.ManyToManyField(blank=True, null=True, to='food.Customer'),
        ),
    ]