from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('',views.gallery_list,name= 'gallery_list'),
    path('<int:id>/',views.gallery_detail,name='gallery_detail')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)