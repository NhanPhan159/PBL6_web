from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=20)
    university = models.CharField(max_length=100)
    major = models.CharField(max_length=100)

class Publication(models.Model):
    title = models.CharField(max_length=100, null=False)
    fields = models.CharField(max_length=100)
    abstract = models.CharField(max_length=10000)
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
