from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
import datetime
class Category(models.Model):
    name = models.CharField(max_length=100)
    imageField = models.ImageField(upload_to='assets/category', default='')
    def __str__(self):
        return self.name


class MenuElements(models.Model):
    fileLink = models.FileField(upload_to='assets/')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default='')
    startDate = models.DateTimeField(auto_now_add=False, editable=True, null=True)
    endDate = models.DateTimeField(auto_now_add=False, editable=True, null=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name