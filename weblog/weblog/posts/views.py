from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Post, PostMedia, Tag


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"  # you will create this template
    context_object_name = "posts"
    paginate_by = 5  # show 5 posts per page

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by("-created_at")


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"  # you will create this template
    context_object_name = "post"

    def get_object(self):
        return get_object_or_404(Post, slug=self.kwargs["slug"], published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all media related to this post
        context['media_items'] = PostMedia.objects.filter(post=self.get_object())
        return context
    
    class TaggedPostListView(ListView):
        model = Post
        template_name = "posts/post_list.html"
        context_object_name = "posts"

        def get_queryset(self):
            self.tag = get_object_or_404(Tag, slug=self.kwargs["slug"])
            return Post.objects.filter(tags=self.tag, published=True)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["tag"] = self.tag
            return context
        

class TaggedPostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs["slug"])
        return Post.objects.filter(tags=self.tag, published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context
    

class TagListView(ListView):
    model = Tag
    template_name = "posts/tag_list.html"
    context_object_name = "tags"
    queryset = Tag.objects.all().order_by("name") 