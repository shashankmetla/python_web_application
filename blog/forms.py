from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "image", "category", "summary", "content", "draft")

        error_messages = {
            "title": {"required": "Please provide a title"},
            "image": {"required": "An image will be great to add"},
            "category": {"required": "Select a category from the drop-down"},
            "summary": {"required": "Please provide a short summary to your post"},
            "content": {"required": "Please provide content to your post"},
        }

        def __init__(self, *args, **kwargs):
            super(CreatePostForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].required = True
