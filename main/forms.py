from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):

    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category', 'tags']
# в. а.

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreatePostForm, self).__init__(*args, **kwargs)

    def clean(self):
        user = self.request.user
        self.cleaned_data['author'] = user
        super(CreatePostForm, self).clean()


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category', 'tags']
