from django.views.generic import TemplateView
from posts.models import Post

class HomePageView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Show recent posts on the homepage
        context["latest_posts"] = Post.objects.filter(published=True).order_by("-created_at")[:5]
        return context
