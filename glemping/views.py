from django.shortcuts import render, get_object_or_404
from .models import Post, Activity


def homepage_view(request):
    return render(request, 'glemping/home.html', {'section': 'home'})


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'glemping/news/list.html',
                  {'posts': posts, 'section': 'news'})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'glemping/news/detail.html', {'post': post})


def activity_list(request):
    activities = Activity.published.all()
    return render(request,
                  'glemping/activities/list.html',
                  {'activities': activities,
                   'section': 'activities'})
