from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from blog.views import post_list, post_details

urlpatterns = [
    url(r'^posts/$', post_list.PostList.as_view()),
    url(r'^posts/(?P<id>[0-9]+)$', post_details.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
