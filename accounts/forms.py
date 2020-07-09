from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Classes


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


'''class ClassesForm(ModelForm):
    class Meta:
        model = Classes
        fields = ('classes','code','teacher','subject')
        labels = {'classes':'Class Name','teacher': 'Teacher Name','code':'Class Code'}'''

class ClassesForm(forms.Form):
    classes = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Class name'}))
    teacher = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Teacher\'s name'}))
    subject = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Subject'}))

class NotesForm(forms.Form):
    title = forms.CharField(max_length=30, label='Title')
    file = forms.FileField(label='Upload File',required=False)
    desc = forms.CharField(label='Description',widget=forms.Textarea)