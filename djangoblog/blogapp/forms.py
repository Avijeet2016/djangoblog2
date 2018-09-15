from django import forms
from . models import Article, Author, Comment, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'body',
            'image',
            'category',
        ]

class registerUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]

class createAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'profile_picture',
            'details',
        ]


class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'email',
            'post_comment',
        ]


class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
