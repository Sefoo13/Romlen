from django.db import models

from firstapp.models.company import Company


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=30)
    count = models.IntegerField()

    def __str__(self):
        return self.name
