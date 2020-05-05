from django.contrib import admin
from django.urls import path, include
from up_auth import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("up_auth.urls")),
    path("user/logout/", views.user_logout, name="logout"),
]
