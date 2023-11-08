

from .models import Comment
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ('full_name','email','ratting','text')
        exclude = ['movie','tarih']

        labels= {
            'full_name':'Your Name',
            'email':'Your Email',
            'ratting':'Rating',
            'text':'Review'
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'ratting': forms.Select(attrs={'class':'form-select'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
            
        }
