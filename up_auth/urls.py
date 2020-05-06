from django.urls import path
from . import views

from up_auth.views import (
    PostCrate,
    PostDelete,
    PostDetail,
    PostList,
    PostUpdate,
    LoginView,
    index,
)

# app_name = 'up_auth'

urlpatterns = [
    # POST VIEWS URL
    path("index/", views.index, name="index"),
    path("", PostList.as_view(), name="post_list"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:slug>/", PostDelete.as_view(), name="post_delete"),
    path("create/new/", PostCrate.as_view(), name="post_create"),
    path("update/<slug:slug>/", PostUpdate.as_view(), name="post_update"),
    # Auth View url
    path("up_auth/user_login/", LoginView.as_view(), name="user_login"),
]
