from django.db import models
from clients.models import Order

class Bottle(models.Model):   
    volume = models.IntegerField(default=10)
    maker = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    expired = models.BooleanField(default=False)


class BottlesCount(models.Model):
    bottle = models.ForeignKey(to=Bottle, on_delete=models.SET_NULL, null=True, blank=True, related_name="bottle")   
    count = models.IntegerField()
    order = models.ForeignKey(to=Order, on_delete=models.SET_NULL, null=True, blank=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bottle} - {self.order}:"