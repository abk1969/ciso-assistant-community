# Generated by Django 5.1.1 on 2024-12-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ebios_rm", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roto",
            name="target_objective",
            field=models.TextField(verbose_name="Target objective"),
        ),
    ]
