from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import Another, BookViewSet, first

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('another', Another.as_view()),
    path('first', first),
    path('', include(router.urls)),
]