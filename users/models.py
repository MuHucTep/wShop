from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    cart_id = models.IntegerField(null=False, blank=True)

    def __str__(self):
        return f'{self.id} {self.name} {self.second_name}'
