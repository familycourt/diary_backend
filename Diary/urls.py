from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.diary.urls')),
    path('', include('apps.qna.urls')),
    path('', include('apps.authentication.urls')),
]
