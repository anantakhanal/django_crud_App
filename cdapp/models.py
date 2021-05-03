from django.db import models


class Entry(models.Model):
    ID = models.CharField(max_length=10,primary_key =True)
    Name = models.CharField(max_length=150)
    data1 = models.CharField(max_length=50)
    data2 = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

# Create your models here.
