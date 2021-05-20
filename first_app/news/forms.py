from django import forms

from .models import News, Commentaries

class NewsForm(forms.Form):
    article = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class NewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'article',
            'body'
        ]
    
    def clean_article(self):
        data = self.cleaned_data.get('article')
        if len(data) < 5:
            raise forms.ValidationError('Article isn`t long enough')
        elif len(data) > 20:
            raise forms.ValidationError('Article is too long')
        return data
    
    def clean_body(self):
        data = self.cleaned_data.get('body')
        if len(data) > 75:
            raise forms.ValidationError('Body is too long')
        return data

class CommentaryModelForm(forms.ModelForm):
    class Meta:
        model = Commentaries
        fields = [
            'text'
        ]

    