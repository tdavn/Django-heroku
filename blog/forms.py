from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )


class PostForm(forms.ModelForm):
    """Used in adding post or update post """
    class Meta:
        model = Post
        fields = ('title', 'categories', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # class from bootstrap form element
            'categories': forms.SelectMultiple(choices=list(choices), attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-group'}),
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'categories', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
            'placeholder': 'This is a title placeholder'}),  # class from bootstrap form element
            'categories': forms.SelectMultiple(choices=list(choices), attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),  # if use own css, can replace here
            'body': forms.Textarea(attrs={'class': 'form-control'}),  # check attrs can be parsed here
        }
