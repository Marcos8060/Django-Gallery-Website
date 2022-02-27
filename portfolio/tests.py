from django.test import TestCase
from .models import Location,Image,Category

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(location='Nairobi',category='Travel',name='Pyramids',description='The best place to visit in Egypt',image='black.png')

# testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

 # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


# Test for Category
class ImageTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='Travel')

# testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

 # Testing Save Method
    def test_save_method(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

# Test for Location
class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')

# testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

 # Testing Save Method
    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

