from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    PostCreateView,
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    )

urlpatterns = [
    url(r'^posts/$', PostListView.as_view()),
    url(r'^posts/create$', PostCreateView.as_view()),
    url(r'^posts/(?P<pk>\d+)$', PostDetailView.as_view()),
    url(r'^posts/(?P<pk>\d+)/edit$', PostUpdateView.as_view()),
    url(r'^posts/(?P<pk>\d+)/delete$', PostDeleteView.as_view()),
]


