from django.urls import path
from .views import PostListView, PostDetailView, TaggedPostListView, TagListView

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tag/<slug:slug>/", TaggedPostListView.as_view(), name="post_by_tag"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
]