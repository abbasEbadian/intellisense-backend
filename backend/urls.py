from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='api/v1/admin/')),
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/api-auth/', include('rest_framework.urls')),
    path('api/v1/summernote/', include('django_summernote.urls')),
    path('api/v1/', include('backend.api'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
