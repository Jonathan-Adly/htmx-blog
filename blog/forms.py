from django import forms
from .models import Blog
from django.urls import reverse_lazy


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "content")
        link = reverse_lazy("preview")
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "h-400",
                    "hx-post": link,
                    "hx-trigger": "keyup changed delay:500ms",
                    "hx-target": "#preview",
                }
            )
        }
