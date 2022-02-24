from django.urls import reverse
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

    def get_absolute_url(self):
        return reverse('gallery_by_category',args=[self.slug])

class Image(models.Model):
    location = models.ForeignKey(Location,on_delete=models.CASCADE) # one image belongs to a single location
    category = models.ForeignKey(Category,on_delete=models.CASCADE) # one image belongs to a single category
    name= models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to = 'articles/',blank=True)

    def get_absolute_url(self):
        return reverse('gallery_detail',args=[self.id])
