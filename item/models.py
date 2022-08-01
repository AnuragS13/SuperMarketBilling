from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    subcategory = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return "{}".format(self.name)
