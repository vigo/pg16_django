from django.conf import settings
from django.conf.urls import url, static
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.PostList.as_view(), name="post-list"),
    url(r'^ekle/?$', views.PostCreate.as_view(), name="post-create"),
    url(r'^detay/(?P<pk>\d+)/?$', views.PostDetail.as_view(), name="post-detail"),
    url(r'^detay/(?P<pk>\d+)/duzenle/?$', views.PostUpdate.as_view(), name="post-update"),
    url(r'^detay/(?P<pk>\d+)/sil/?$', views.PostDelete.as_view(), name="post-delete"),
]

