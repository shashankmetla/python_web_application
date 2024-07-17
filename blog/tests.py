from django.test import TestCase
from .models import Post, Category
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify


class PostModelTests(TestCase):
    def test_create_post(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="vivek",
            first_name="Vivek",
            last_name="Singh",
            email="vivek@gmail.com",
            password="pass12345",
            line="adderess line",
            city="user city",
            state="user state",
            pincode=226006,
            is_doctor=True,
        )
        category = Category.objects.create(
            name="new category", slug=slugify("new category")
        )
        post = Post.objects.create(
            title="Post title",
            summary="post summary",
            content="post content",
            category=category,
            slug=slugify("Post title"),
            written_by=user,
        )

        self.assertEqual(post.title, "Post title")
        self.assertEqual(post.summary, "post summary")
        self.assertEqual(post.content, "post content")
        self.assertEqual(post.written_by, user)
        self.assertEqual(post.category, category)
