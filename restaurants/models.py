from django.db import models

# Create your models here.
class restaurant(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=200)
    opening_time=models.TimeField(auto_now=False,auto_now_add=False)
    closing_time=models.TimeField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return "restaurant: " + self.name 