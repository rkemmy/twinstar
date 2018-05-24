from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.CharField(max_length = 256)
    user = models. OneToOneField(User, on_delete=models.CASCADE)
    website = forms.URLField(initial='http://')
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)





class Image(models.Model):
    image = models.ImageField(upload_to='gallery/')
    name = models.CharField(max_length = 30)
    owner = models. ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        photo = cls.objects.all()
        return photo

    class Meta:
        ordering = ['name']