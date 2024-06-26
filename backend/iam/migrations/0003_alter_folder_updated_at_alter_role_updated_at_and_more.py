# Generated by Django 5.0.4 on 2024-04-30 21:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("iam", "0002_purge_validator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="folder",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="role",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="roleassignment",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="usergroup",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
    ]
