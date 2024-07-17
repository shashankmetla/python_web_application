from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, null=True)
    image = models.ImageField(upload_to="blog/")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    summary = models.TextField()
    content = models.TextField()
    draft = models.BooleanField(default=True)
    written_by = models.ForeignKey("main.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:40]

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ("created_at",)
