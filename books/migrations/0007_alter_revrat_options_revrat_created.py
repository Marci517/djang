# Generated by Django 5.0.7 on 2024-07-25 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0006_revrat"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="revrat",
            options={"ordering": ["-created"]},
        ),
        migrations.AddField(
            model_name="revrat",
            name="created",
            field=models.DateTimeField(default=datetime.date(2024, 7, 25)),
        ),
    ]