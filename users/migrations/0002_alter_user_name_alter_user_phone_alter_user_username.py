# Generated by Django 4.1.3 on 2022-11-03 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=100, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(max_length=20, verbose_name="phone"),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.EmailField(
                max_length=150, unique=True, verbose_name="username"
            ),
        ),
    ]
