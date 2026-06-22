from django.db import models

class GiftModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
