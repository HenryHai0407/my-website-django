from django.db import models

# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
