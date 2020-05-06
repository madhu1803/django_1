from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from user_post_auth.settings import (
    DEBUG,
    STATIC_URL,
    STATIC_ROOT,
    MEDIA_URL,
    MEDIA_ROOT,
)

from up_auth import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("up_auth.urls")),
    path("user/logout/", views.user_logout, name="logout"),
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
