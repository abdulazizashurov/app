from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('abdu/', admin.site.urls),

    path('',include('main.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

