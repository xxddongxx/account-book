# Generated by Django 4.1.3 on 2022-11-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_name_alter_user_phone_alter_user_username"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="user",
            name="name",
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=120, unique=True, verbose_name="이메일"),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.EmailField(max_length=150, verbose_name="유저명"),
        ),
    ]
