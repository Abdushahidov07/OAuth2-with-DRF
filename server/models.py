from django.db import models


class Cars(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    prodect_year = models.IntegerField()

    def __str__(self):
        return self.name
    
