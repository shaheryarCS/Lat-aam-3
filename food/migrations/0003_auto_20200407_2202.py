# Generated by Django 3.0.4 on 2020-04-07 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20200405_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appti',
            name='price',
        ),
        migrations.RemoveField(
            model_name='main_menu',
            name='price',
        ),
        migrations.RemoveField(
            model_name='sweet',
            name='price',
        ),
        migrations.CreateModel(
            name='Price_Sweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('sweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Sweet')),
            ],
        ),
        migrations.CreateModel(
            name='Price_MainMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('main_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Main_menu')),
            ],
        ),
        migrations.CreateModel(
            name='Price_Apptiti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('apptitzer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Appti')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('Cost', models.IntegerField(default=0)),
                ('time', models.TimeField(auto_now=True)),
                ('customer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Customer')),
                ('packages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Package')),
            ],
        ),
        migrations.CreateModel(
            name='Day_Sweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_No', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('sweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Sweet')),
            ],
        ),
        migrations.CreateModel(
            name='Day_MainMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_No', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('main_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Main_menu')),
            ],
        ),
        migrations.CreateModel(
            name='Day_Apptiti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_No', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('apptitzer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Appti')),
            ],
        ),
    ]
