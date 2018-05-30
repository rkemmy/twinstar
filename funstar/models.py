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
    owner = models. ForeignKey(User,on_delete=models.CASCADE,default=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,default=True)
    caption = models.TextField(max_length = 200)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        photo = cls.objects.all()
        return photo

    class Meta:
        ordering = ['name']

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Image,on_delete=models.CASCADE)
    comment_content = models.TextField(blank=True)


    def __str__(self):
        return self.comment_content

    @classmethod
    def get_post_comments(cls,post_id):
        post_comments = Comment.objects.filter(post=post_id)
        return post_comments