from unicodedata import category
from django.shortcuts import get_object_or_404, render
from .models import Image,Category,Location

# Create your views here.
def gallery_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    images = Image.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        images = images.filter(category=category)
    return render(request,'index.html',{'categories':categories,
                                         'category':category,
                                          'images':images
                                        })

def gallery_detail(request,id):
    images = get_object_or_404(Image,id=id)
    return render(request,'gallery_detail.html',{'images':images})

