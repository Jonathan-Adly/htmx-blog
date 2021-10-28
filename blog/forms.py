from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "content")

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "h-400",
                    "hx-post": "/preview",
                    "hx-trigger": "keyup changed delay:500ms",
                    "hx-target": "#preview",
                }
            )
        }
