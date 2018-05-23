from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.CharField(max_length = 256)
    user = models. ForeignKey(User, on_delete=models.CASCADE)
    website = forms.URLFiels(initial='http://')
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)

    def __str__(self):
        return self.user


class Image(models.Model):
    image = models.ImageField(upload_to='gallery/')
    name = models.CharField(max_length = 30)
    owner = models. ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']