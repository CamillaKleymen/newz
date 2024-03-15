from django import forms
from .models import NewsModel

class News(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ('news_title', 'news_category', 'news_description')
