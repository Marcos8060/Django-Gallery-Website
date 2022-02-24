from django.db import models

# Create your models here
class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    location = models.ForeignKey(Location,on_delete=models.CASCADE) # one image belongs to a single location
    category = models.ForeignKey(Category,on_delete=models.CASCADE) # one image belongs to a single category
    name= models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to = 'articles/',blank=True)
