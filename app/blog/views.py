from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create the post list view (david.ingledow.co.uk/blog)
def index(request):
        # get the blog posts that are published
        posts = Post.objects.filter(published=True).order_by('-pub_date')
        # now return the rendered template
        return render(request, 'blog/index.html', {'post': posts})

def post(request, slug):
        # get the Post object
        post = get_object_or_404(Post, slug=slug)
        # now return the rendered template
        return render(request, 'blog/single.html', {'post': post})

def about(request):
        # get the blog posts that are published
        posts = Post.objects.filter(published=True).order_by('-pub_date')
        # now return the rendered template
        return render(request, 'blog/about.html', {'post': posts})
