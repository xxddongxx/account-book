# Generated by Django 4.1.3 on 2022-11-22 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_managers_remove_user_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=150, verbose_name="유저명"),
        ),
    ]
