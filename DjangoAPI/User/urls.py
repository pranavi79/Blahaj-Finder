from django.conf.urls import url
from User import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^blahaj$',views.blahajApi),
    url(r'^blahaj/([0-9]+)$',views.blahajApi),

    url(r'^user$',views.usersApi),
    url(r'^user/([0-9]+)$',views.usersApi),

    url(r'^user/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)