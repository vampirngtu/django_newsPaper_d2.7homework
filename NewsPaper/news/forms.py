from django.forms import ModelForm
from .models import Post, Author
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'zagolovok', 'novosti', 'rating', 'post_type', 'postCategory']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя Автора'
            }),
            'zagolovok': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'novosti': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'rating': forms.TextInput(attrs={
                'type': 'number',
                'class': 'form-control',
                'value': 0
            }),
            'post_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'postCategory': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'категория новостей'
            }),
        }
