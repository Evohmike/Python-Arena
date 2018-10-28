from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import(
    PostCreateView,
    CommentCreateView
)

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^post/new/', PostCreateView.as_view(),name='post-create'),
    url(r'^comment/new/',CommentCreateView.as_view(),name='comment-created'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

