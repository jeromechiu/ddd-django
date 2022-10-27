from django.db import models


class MyProd(models.Model):
    pid = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    name = models.CharField(max_length=50)
    amount = models.PositiveIntegerField(default=0)
    place = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now=True)
    deletable = models.BooleanField(default=True)

    class Meta:
        ordering = ["create_date"]
