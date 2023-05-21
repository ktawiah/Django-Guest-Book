from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
    )
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": "5",
                "id": "comment",
                "placeholder": "Comment",
            }
        )
    )

    class Meta:
        model = Comment
        fields = [
            "name",
            "comment",
        ]
