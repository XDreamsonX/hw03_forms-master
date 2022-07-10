from django.forms import ModelForm
from .models import Post
from django import forms


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['text', 'group']

    def clean_data(self):
        text = self.cleaned_data['text']
        if text == '':
            raise forms.ValidationError('Пост не может быть без текста')
        return text
