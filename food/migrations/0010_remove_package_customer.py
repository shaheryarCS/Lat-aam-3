# Generated by Django 3.0.4 on 2020-04-19 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_auto_20200419_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='customer',
        ),
    ]
