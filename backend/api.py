from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog import views as blog_views
from manager import views as manager_views
from contact import views as contact_views
from config import views as config_views

# from contact.serializers import ContactSerializer
# from rest_framework import generics
# from contact.models import Contact

router = routers.DefaultRouter()
router.register(r'blogs', blog_views.BlogViewSet)
router.register(r'blog_categories', blog_views.BlogCategoryViewSet)


router.register(r'managers', manager_views.MangerViewSet)
router.register(r'contacts', contact_views.ContactViewSet)
router.register(r'roadmaps', config_views.RoadmapViewSet)
router.register(r'utils', config_views.UtilViewSet)
router.register(r'faq', config_views.FAQViewSet)
router.register(r'centeralized', config_views.CenterViewSet)




urlpatterns = [
    path('', include(router.urls)),
    # path('contact/', generics.ListCreateAPIView.as_view(queryset=Contact.objects.all(), serializer_class=ContactSerializer), name='contact-list')

]