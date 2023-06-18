from django.urls import path, re_path
from .views import PostList, PostDetail, UserPostList

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
    re_path('^user/(?P<username>.+)/$', UserPostList.as_view()),
]
