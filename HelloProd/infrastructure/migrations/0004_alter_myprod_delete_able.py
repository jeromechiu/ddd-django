# Generated by Django 4.1.1 on 2022-09-27 06:26
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("HelloProd", "0003_alter_myprod_delete_able"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myprod",
            name="delete_able",
            field=models.BooleanField(default=True),
        ),
    ]