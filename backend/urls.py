from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('api/v1/', include('backend.api'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
