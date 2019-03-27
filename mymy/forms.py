from django import forms

from .models import Post, Search

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class LoL(forms.ModelForm):
    class summoner:
        model = Search
        fields = ('name', 'tier')