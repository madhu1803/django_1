from django.urls import path
from . import views
from user_post_auth.settings import (
    DEBUG,
    STATIC_URL,
    STATIC_ROOT,
    MEDIA_URL,
    MEDIA_ROOT,
)
from django.conf.urls.static import static
from up_auth.views import (
    PostCrate,
    PostDelete,
    PostDetail,
    PostList,
    PostUpdate,
    LoginView,
)

# app_name = 'up_auth'

urlpatterns = [
    # POST VIEWS URL
    path("", PostList.as_view(), name="post_list"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:slug>/", PostDelete.as_view(), name="post_delete"),
    path("create/new/", PostCrate.as_view(), name="post_create"),
    path("update/<slug:slug>/", PostUpdate.as_view(), name="post_update"),
    # Auth View url
    path("up_auth/user_login/", LoginView.as_view(), name="user_login"),
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
