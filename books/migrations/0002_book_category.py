# Generated by Django 5.0.7 on 2024-07-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="category",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
