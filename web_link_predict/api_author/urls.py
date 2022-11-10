from rest_framework import routers
from api_author.views import Authorviewset
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r"", Authorviewset)
urlpatterns = [
    path('',include(router.urls))
    ]