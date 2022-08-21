from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog import views as blog_views
from manager import views as manager_views

router = routers.DefaultRouter()
router.register(r'blogs', blog_views.BlogViewSet)
router.register(r'blog_categories', blog_views.BlogCategoryViewSet)


router.register(r'managers', manager_views.MangerViewSet)

urlpatterns = [
    path('', include(router.urls))
]