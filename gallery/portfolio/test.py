# <!-- <li><a class="dropdown-item" href="{% url 'gallery_list' %}">All</a></li> -->
    # path('',views.gallery_list,name='gallery_by_category'),


# def gallery_list(request,category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     images = Image.objects.all()
#     if category_slug:
#         category = get_object_or_404(Category,slug=category_slug)
#         images = images.filter(category=category)
#     return render(request,'category.html',{'categories':categories,
#                                          'category':category,
#                                           'images':images
#                                         })
