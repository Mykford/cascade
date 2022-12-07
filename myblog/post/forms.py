from django import forms
from .models import Posts , Categories

query_choices = Categories.objects.all().values_list('name','name') # Getting all category object in model
categor_choices = [] #creating an empty list 
for i in query_choices: 
    categor_choices.append(i) # appending values in list into  empty list

# Post Creation form
class CreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title','author','body','category','status']
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'thisuser','type':'hidden'}),
             'author': forms.Select(attrs={'class':'form-select'}),
            'category':forms.Select(choices=categor_choices,attrs={'class':'form-select'}),
            'body': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder': 'Type Your Blog Here'}),
            'status': forms.Select(attrs={'class': 'form-select'})    
        }
        
        # Post Editing Form
class EditForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title','body']
        widgets = {
            'title':forms.TextInput(attrs={'class' : 'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
             'category':forms.Select(choices=categor_choices,attrs={'class':'form-select'})
        }
