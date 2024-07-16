from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sqlapp.urls')),  # Include the urls from the sqlapp application
    path('cms/', include('blog.urls')), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
