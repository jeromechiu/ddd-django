# Generated by Django 4.1.1 on 2022-09-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyProd',
            fields=[
                ('pid', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('place', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['create_date'],
            },
        ),
    ]
