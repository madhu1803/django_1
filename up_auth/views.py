from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    CreateView,
    FormView,
)
from .models import Post
from .forms import PostCreate, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# POST VIEWS - CRUD
# LIST VIEW
class PostList(LoginRequiredMixin, ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post/post_list.html"


# DETAIL VIEW
class PostDetail(DetailView):
    model = Post
    template_name = "post/post_detail.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostDetail, self).dispatch(*args, **kwargs)


# CREATE VIEW
class PostCrate(CreateView):
    form_class = PostCreate
    template_name = "post/post_form.html"
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostCrate, self).dispatch(*args, **kwargs)


# UPDATE VIEW
class PostUpdate(UpdateView):
    form_class = PostCreate
    template_name = "post/post_form.html"
    queryset = Post.objects.all()
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostUpdate, self).dispatch(*args, **kwargs)


# DELETE VIEW
class PostDelete(DeleteView):
    model = Post
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostDelete, self).dispatch(*args, **kwargs)


# AUTHENTICATION
# login view
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user_login"))


# logout view
class LoginView(FormView):
    template_name = "up_auth/login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        username = form.data["username"]
        password = form.data["password"]

        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return HttpResponseRedirect(reverse("post_list"))
        else:
            return HttpResponse("Invalid login details given")
