from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Post, Category
from django.template.defaultfilters import slugify
from .forms import CreatePostForm
from django.contrib.auth.mixins import UserPassesTestMixin


class AllCategories(ListView):
    model = Category
    template_name = "categories.html"


class CategoryPost(ListView):
    template_name = "posts_category.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]
        category = Category.objects.get(slug=slug)
        context["posts"] = Post.objects.filter(category=category, draft=False)
        return context


class PostCreate(UserPassesTestMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "create_post.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.slug = slugify(post.title)
        post.written_by = self.request.user
        post.save()
        return redirect("/")

    def test_func(self):
        return self.request.user.is_doctor


class PostDetail(DetailView):
    model = Post
    template_name = "single_post.html"


class DraftPostList(UserPassesTestMixin, ListView):
    model = Post
    template_name = "drafts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().filter(
            written_by=self.request.user, draft=True
        )
        return context

    def test_func(self):
        return self.request.user.is_doctor


class PostUpdate(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ["title", "summary", "image", "content", "category", "draft"]

    def test_func(self):
        return self.request.user.is_doctor
