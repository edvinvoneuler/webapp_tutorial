from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import Another, BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('another', Another.as_view()),
    path('', include(router.urls)),
]