
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('meals/',include('meals.urls', namespace = 'meals')),
    path('',include('home.urls', namespace = 'home')),
    path('blog/',include('blog.urls', namespace = 'blog')),
    path('contact/',include('contact.urls', namespace = 'contact')),
    path('about-us/',include('aboutus.urls', namespace = 'aboutus')),
    path('reserve_table/',include('reservation.urls', namespace = 'reservation')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'restaurants Mrakkchi Admin'