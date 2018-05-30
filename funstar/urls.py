from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/profile/edit/$',views.edit_profile,name='edit_profile'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^add/(\d+)', views.comment, name='comment'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)