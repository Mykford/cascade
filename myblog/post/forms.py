from django import forms
from .models import Posts

class CreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title','author','body','status']
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class':'form-select'}),
            'body': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder': 'Type Your Blog Here'}),
            'status': forms.Select(attrs={'class': 'form-select'})    
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title','body']
        widgets = {
            'title':forms.TextInput(attrs={'class' : 'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'})
        }
