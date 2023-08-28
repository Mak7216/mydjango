from django import forms
from .models import Post
from news.models import News

class PostForm(forms.ModelForm):
    class Meta:
            model = Post
            fields = ('title', 'body', )
            labels = {
                'title': ('Заголовок'),
                'body': ('Содержание'),

            }
class NewsForm(forms.ModelForm):
    class Meta:
            model = News
            fields = ('title', 'body', )
            labels = {
                'title': ('Заголовок'),
                'body': ('Содержание'),

            }