from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_txt", )
        widgets = {
            'comment_txt': forms.Textarea(
                attrs={
                    'placeholder': 'Enter your comment...',
                }),
        }
