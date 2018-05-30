from django import forms
from .models import Profile, Image, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['date','user_name','user']

class ImageUpload(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['post_date','profile','owner',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','post']
