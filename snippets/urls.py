# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('snippets', views.SnippetViewSet)
router.register('user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]