from django.urls import path
from .views import PostListView, PostDetailView, TaggedPostListView

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("tag/<slug:slug>/", TaggedPostListView.as_view(), name="post_by_tag"),
]
