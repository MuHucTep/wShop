from django.db import models

class GiftModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    category_id = models.IntegerField(null=False, blank=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class CategoryModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=True)

    def __str__(self):
        return self.name
