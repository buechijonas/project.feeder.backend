# Generated by Django 4.1.7 on 2023-04-24 15:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("commentary", "0002_alter_commentary_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentary",
            name="text",
            field=models.TextField(max_length=200, verbose_name="Inhalt"),
        ),
    ]
